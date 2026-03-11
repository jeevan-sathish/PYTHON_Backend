from mcp.server.fastmcp import FastMCP


mcp =FastMCP("my server")

@mcp.tool()
def demo(name:str)->str:
    print(name)

if __name__=="__mian__":
    mcp.run()
    