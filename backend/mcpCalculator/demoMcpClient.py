from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio


async def main():
    server = StdioServerParameters(
        command="python",                 # fixed: command not commands
        args=["demoMcpServer.py"]         # fixed: removed starting /
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            # optional but recommended
            tools = await session.list_tools()
            print("Available tools:", tools)

            result = await session.call_tool(
                "demo",
                {"name": "jeevan"}
            )

            print("result:", result.content[0].text)   # fixed typo


asyncio.run(main())