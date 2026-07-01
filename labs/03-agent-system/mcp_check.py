"""List the tools the local MCP server exposes — no LLM required.

The fastest way to confirm the MCP wiring works before running the full agent:
`make mcp-check`. If this prints the tools, the server + client are talking.
"""

import asyncio
import sys

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "orders": {
                "command": sys.executable,
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )
    tools = await client.get_tools()
    print("MCP tools available:")
    for t in tools:
        print(f"  - {t.name}: {t.description}")


if __name__ == "__main__":
    asyncio.run(main())
