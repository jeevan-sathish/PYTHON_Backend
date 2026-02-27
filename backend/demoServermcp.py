from mcp.server.fastmcp import FastMCP



mcp = FastMCP("my mcp server")

@mcp.tool()

def getName(name:str)->str:
    return f"this is {name}"

if __name__ == "__main__":
    mcp.run()