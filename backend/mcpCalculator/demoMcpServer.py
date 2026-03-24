from mcp.server.fastmcp import FastMCP


mcp = FastMCP("my mcp server")

@mcp.tool()
def greet(name:str)->str:
    return f"hello {name}"


if __name__=="__main__":
    mcp.run()