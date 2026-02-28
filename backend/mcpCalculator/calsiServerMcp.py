from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Calculator MCP Server")

@mcp.tool()
def calculate(expression: str) -> float:
   


    expression = expression.replace(" ", "")

    operators = ["+", "-", "*", "/"]

    try:
        for op in operators:
            if op in expression:
                num1, num2 = expression.split(op)

                num1 = float(num1)
                num2 = float(num2)

                if op == "+":
                    return num1 + num2
                elif op == "-":
                    return num1 - num2
                elif op == "*":
                    return num1 * num2
                elif op == "/":
                    if num2 == 0:
                        return "Error: Division by zero"
                    return num1 / num2

        return "Invalid expression format"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()