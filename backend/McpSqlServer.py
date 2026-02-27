from mcp.server.fastmcp import FastMCP
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("My Mcp Sql Server")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

print("Connection successful")

@mcp.tool()
def addName(name: str) -> str:
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO names(name) VALUES (%s)"
            cursor.execute(query, (name,))
            conn.commit()
        return f"{name} added successfully"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()