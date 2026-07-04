"""Lab 07 · Capstone — a support-assistant agent, the whole stack assembled.

Hub-and-spoke orchestrator-worker (same shape as Lab 03), with two spokes:

  - search_docs   — the RAG tool (Lab 02's hybrid retrieval + rerank, Lab 07's corpus)
  - lookup_order  — the MCP tool (Lab 03's "orders" server, reused for continuity)

The whole invocation is wrapped in one Langfuse trace (Lab 06's pattern, applied
at the agent level rather than per-node — see the README's go-deeper note for how
you'd add per-node spans too). Provider-agnostic (see labs/model-backends.md).
Run with `make run` or `python agent.py "your question"`.
"""

import asyncio
import sys

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langfuse import Langfuse
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

import provider
from rag_tool import search_docs

load_dotenv()

langfuse = Langfuse()  # reads LANGFUSE_PUBLIC_KEY / LANGFUSE_SECRET_KEY / LANGFUSE_HOST from env

SYSTEM_PROMPT = (
    "You are a support assistant with two tools: search_docs (policy questions) "
    "and lookup_order (order status). When a question has multiple parts, call "
    "every tool needed, then address every part in your final answer - don't "
    "drop a part just because another tool call also returned useful information."
)


async def build_agent():
    mcp_client = MultiServerMCPClient(
        {
            "orders": {
                "command": sys.executable,
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )
    mcp_tools = await mcp_client.get_tools()
    tools = [search_docs, *mcp_tools]  # spokes: RAG + MCP order lookup

    llm = provider.get_chat_model().bind_tools(tools)

    def orchestrator(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}

    graph = StateGraph(MessagesState)
    graph.add_node("orchestrator", orchestrator)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge(START, "orchestrator")
    graph.add_conditional_edges("orchestrator", tools_condition)
    graph.add_edge("tools", "orchestrator")
    return graph.compile()


async def ask(query: str):
    agent = await build_agent()

    with langfuse.start_as_current_observation(name="capstone-ask", as_type="span", input=query) as trace:
        trace_id = trace.trace_id
        result = await agent.ainvoke(
            {
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query},
                ]
            }
        )
        final = result["messages"][-1].content
        trace.update(output=final)

    langfuse.flush()
    try:
        trace_url = langfuse.get_trace_url(trace_id=trace_id)
    except Exception:
        trace_url = None

    return result, trace_url


async def main():
    query = " ".join(sys.argv[1:]) or (
        "What's your return policy, and what's the status of order A100?"
    )
    result, trace_url = await ask(query)

    for m in result["messages"]:
        m.pretty_print()

    print()
    if trace_url:
        print(f"Trace: {trace_url}")
    else:
        print("Trace: not available (set LANGFUSE_PUBLIC_KEY/SECRET_KEY in .env to see it in a dashboard)")


if __name__ == "__main__":
    asyncio.run(main())
