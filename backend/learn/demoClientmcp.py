import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    
    server =StdioServerParameters(
        command="python",
        args=["demoServermcp.py"]
    )
    
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
            
            await session.initialize()
            
            result = await session.call_tool("getName",{"name":"jeevan"})
            
            print("session called:",result.content[0].text)

asyncio.run(main())
    