from mpc.server.fastmcp import FastMCP

mcp =FastMCP("my mcp server with ollama")


@mcp.tool
def getResponce(prompt:str)->str:
    return F"this is :{prompt}"

if __name__=="__main__":
    mcp.run()