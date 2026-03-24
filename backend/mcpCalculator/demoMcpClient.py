import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server =StdioServerParameters(
        command="python",
        args=["demoMcpServer.py"]
    )

    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)
            result = await session.call_tool("greet",{"name":"jeevan"})
            print(result.content[0].text)


asyncio.run(main())