from mcp.server.fastmcp import FastMCP
import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

mcp = FastMCP("my mcp server")

@mcp.tool()
def greet(name:str)->str:
    """ this is just a greet name """
    return f"hello {name}"

@mcp.tool()
def add(a:int ,b:int)->int:
    """ add two numbers """
    return a+b
@mcp.tool()
def sub(a:int ,b:int)->int:
    """ subtract two numbers """
    return a-b

@mcp.tool()
def query(prompt:str)->str:
    """General question answering using Groq"""

    client=Groq(api_key=os.getenv("GROQ_API_KEY"))

    response =client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content

if __name__=="__main__":
    mcp.run()