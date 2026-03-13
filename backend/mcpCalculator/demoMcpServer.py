from mcp.server.fastmcp import FastMCP


mcp =FastMCP("my server")

@mcp.tool()
def demo(name:str)->str:
    return f"{name} is my name"

if __name__=="__main__":
    mcp.run()
    