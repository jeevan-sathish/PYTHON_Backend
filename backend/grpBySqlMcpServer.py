from mcp.server.fastmcp import FastMCP
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP("Employee Server")


@mcp.tool()
def getEmpData(id: int) -> str:
    try:
        conn = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )

        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM employe WHERE depID = %s"
        cursor.execute(query, (id,))
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        if data:
            return str(data)
        else:
            return "Employee not found"

    except Exception as e:
        return f"Server Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()