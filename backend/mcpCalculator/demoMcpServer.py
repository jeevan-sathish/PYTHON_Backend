from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my mcp server")

@mcp.tool()
def greet(name:str)->str:
    """ this is just a greet name """
    return f"hello {name}"
@mcp.tool()
def add(a:int ,b:int)->int:
    """ this is addition """
    return a+b

if __name__=="__main__":
    mcp.run()