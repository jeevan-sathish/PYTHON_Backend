from mcp.server.fastmcp import FastMCP
import ollama

mcp =FastMCP("my mcp ollama server")

@mcp.tool()
def getResponse(prompt:str)->str:
    
    response =ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
       
    )
    return response["message"]["content"]

if __name__=="__main__":
    mcp.run()