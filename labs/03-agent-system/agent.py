"""Lab 03 · A hub-and-spoke agent in LangGraph.

An agent is a flowchart the model runs. Here the graph is:

    START -> orchestrator -> (needs a tool?) -> workers(tools) -> orchestrator -> END

The **orchestrator** (an LLM with tools bound) decides, each turn, whether to answer
or to call a worker. The **workers** are the tools — one local Python tool and one
tool reached over MCP (a separate 'orders' server). Results flow back to the
orchestrator, which decides what to do next. That loop *is* the hub-and-spoke
orchestrator-worker pattern.

Provider-agnostic (see labs/model-backends.md). Agents lean on the model's routing,
so use a capable model — llama3.1:8b or a hosted model — for reliable results.
Run with `make run` or `python agent.py "your question"`.
"""

import asyncio
import sys

from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

import provider


# --- A local worker (an ordinary tool the orchestrator can call). --------------
@tool
def word_count(text: str) -> int:
    """Count the number of words in a piece of text."""
    return len(text.split())


async def build_agent():
    # Load the MCP tool(s) from our local 'orders' server. langchain-mcp-adapters
    # launches the server (stdio) and exposes its tools as normal LangChain tools.
    mcp_client = MultiServerMCPClient(
        {
            "orders": {
                "command": sys.executable,      # same interpreter (has `mcp` installed)
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )
    mcp_tools = await mcp_client.get_tools()
    tools = [word_count, *mcp_tools]            # spokes: local + MCP

    # The orchestrator is the model with the tools bound to it.
    llm = provider.get_chat_model().bind_tools(tools)

    def orchestrator(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}

    # Build the graph: orchestrator decides; if it called a tool, run it, then loop.
    graph = StateGraph(MessagesState)
    graph.add_node("orchestrator", orchestrator)
    graph.add_node("tools", ToolNode(tools))     # the workers
    graph.add_edge(START, "orchestrator")
    graph.add_conditional_edges("orchestrator", tools_condition)  # -> "tools" or END
    graph.add_edge("tools", "orchestrator")
    return graph.compile()


async def main():
    query = " ".join(sys.argv[1:]) or (
        "What is the status of order A100, and how many words are in this sentence?"
    )
    agent = await build_agent()
    result = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})

    # Show the full trace so you can see the orchestrator route to workers.
    for m in result["messages"]:
        m.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
