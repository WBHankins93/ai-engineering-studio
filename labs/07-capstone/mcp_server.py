"""A minimal MCP server — the agent reaches your systems through this.

Same "orders" stand-in as Lab 03, reused here so the capstone's two tools
(RAG over docs, and this order lookup) tell one coherent support-assistant story.
Run standalone to sanity-check it: `python mcp_server.py` (it waits on stdio).
The agent (agent.py) launches it automatically.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("orders")


@mcp.tool()
def lookup_order(order_id: str) -> str:
    """Look up the current status of a customer order by its ID (e.g. A100)."""
    fake = {
        "A100": "shipped — arriving Tuesday via UPS",
        "B200": "processing — not yet shipped",
        "C300": "delayed — backordered, ETA 2 weeks",
    }
    return fake.get(order_id.upper(), f"No order found with ID {order_id!r}.")


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
