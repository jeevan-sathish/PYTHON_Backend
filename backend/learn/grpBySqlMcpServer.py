from mcp.server.fastmcp import FastMCP
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Database connection
try:
    conn = mysql.connector.connect(
        user=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    print("Connection successful")
except Exception as e:
    print("Database connection error:", e)

mcp = FastMCP("Employee Server")

@mcp.tool()
def getEmpData(id: int) -> str:
    try:
        cursor = conn.cursor()   # ✅ correct way
        query = "SELECT * FROM employe WHERE id=%s"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        cursor.close()

        if not result:
            return "No employee found"

        return str(result)   # ✅ must return string
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()