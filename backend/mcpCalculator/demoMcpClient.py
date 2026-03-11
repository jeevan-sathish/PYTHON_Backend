from mcp import ClientSession ,StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

async def main():
    server =StdioServerParameters(
        commands="python",
        args=['/backend/mcpCalculator/demoMcpServer.py']
    )
    
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
           await session.initialize()
           result = await session.call_tool("demo",{"name":"jeevan"})
           print("reslut",result.content[0].text)
         
asyncio.run(main())