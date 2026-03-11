from mcp.server.fastmcp import FastMCP


mcp =FastMCP("my server")

@mcp.tool()
def demo(name:str)->str:
    print(name ,"is my name ")
    print("server executed succesfull")

if __name__=="__mian__":
    mcp.run()
    