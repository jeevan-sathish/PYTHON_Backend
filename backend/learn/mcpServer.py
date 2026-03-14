# mcpServer.py

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("TestServer")

# Register tool
@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}, welcome to MCP!"

# Run server
if __name__ == "__main__":
    mcp.run()