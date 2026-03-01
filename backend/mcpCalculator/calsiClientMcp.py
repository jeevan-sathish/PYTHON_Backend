import asyncio

from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server=StdioServerParameters(
        command="python",
        args=["calsiServerMcp.py"]
    ) 
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            expression =input("enter the expression:")
            result = await session.call_tool("calculate",{"expression":expression})
            
            print("the Result:",result.content[0].text)
            
asyncio.run(main())