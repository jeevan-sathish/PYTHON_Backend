import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server =StdioServerParameters(
        command="python",
        args=["calculatorServerMcp.py"]
    )
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
            
            await session.initialize()
            
            result1 = await session.call_tool("add",{"a":10,"b":20})
            result2 = await session.call_tool("sub",{"a":20,"b":5})
            
            print("result is :" ,result1.content[0].text)
            print("result is :" ,result2.content[0].text)
            

asyncio.run(main())
