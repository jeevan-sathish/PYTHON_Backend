import asyncio
import os
import ast
from dotenv import load_dotenv
from groq import Groq
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


def groq_tool(prompt, tools):
    system_prompt = f"""
You are a tool selector.

User prompt:
{prompt}

Available tools:
{tools}

Your job:
1. Read the user prompt carefully.
2. Choose the single best tool from the available tools.
3. Extract the exact argument values needed for that tool from the user prompt.
4. Return the result in exactly this format:

"tool_name", {{"arg1": value1, "arg2": value2}}

Rules:
- Return only one tool.
- Return only the final answer.
- Do not explain anything.
- Do not add markdown.
- Do not add words like Output:
- Do not return JSON array.
- Do not return code block.
- Keep the argument names exactly the same as the selected tool.
- If the selected tool has one argument, return one key only.
- If the user asks for addition, prefer the add tool.
- If the user asks for greeting, prefer the greet tool.
- If no specific tool matches, use query.

Examples:
User: add 5 and 7
Output:
"add", {{"a": 5, "b": 7}}

User: greet jeevan
Output:
"greet", {{"name": "jeevan"}}

User: what is machine learning
Output:
"query", {{"prompt": "what is machine learning"}}
"""

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def parse_tool_response(text):
    tool_name, args_text = text.split(",", 1)
    tool_name = tool_name.strip().strip('"').strip("'")
    args_dict = ast.literal_eval(args_text.strip())
    return tool_name, args_dict


async def main():
    server = StdioServerParameters(
        command="python",
        args=["demoMcpServer.py"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools)

            prompt = input("Enter the prompt: ")

            selected_tool_output = groq_tool(prompt, tools)
            print("LLM selected:", selected_tool_output)

            tool_name, arguments = parse_tool_response(selected_tool_output)

            result = await session.call_tool(tool_name, arguments)

            if result.content and hasattr(result.content[0], "text"):
                print("Result:", result.content[0].text)
            else:
                print("Raw result:", result)


asyncio.run(main())