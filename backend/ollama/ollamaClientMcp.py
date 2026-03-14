from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

async def main():
    server =StdioServerParameters(
        command="python",
        args=["ollamaServerMcp.py"]
    )
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            prompt=str(input("enter the prompt:"))
            result = await session.call_tool("getResponse",{"prompt":prompt})
            print("responce:", result.content[0].text)


asyncio.run(main())