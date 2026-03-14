# mcpClient.py
import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters


async def main():
    # Define server execution command
    server = StdioServerParameters(
        command="python",
        args=["mcpServer.py"]
    )

    # Start stdio connection
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            
            # 🔥 IMPORTANT: Initialize session
            await session.initialize()

            # Call tool
            result = await session.call_tool(
                "greet",
                {"name": "jeevan"}
            )
            
          

            print("Server Response:", result.content[0].text)

asyncio.run(main())