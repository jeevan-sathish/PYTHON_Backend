import mysql.connector
from dotenv import load_dotenv
import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

conn = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

cursor = conn.cursor(dictionary=True)

if conn.is_connected():
    print("Connection successful")

    try:

        def getData():
            query = "SELECT * FROM employe"
            cursor.execute(query)
            rows = cursor.fetchall()
            for data in rows:
                print(data)

        def max_salary():
            query = "SELECT MAX(salary) as Seniour_developer FROM employe"
            cursor.execute(query)
            data = cursor.fetchone()
            print("Highest salary:", data["Seniour_developer"])

        def insert_data():
            try:
                query = "INSERT INTO employe(depID,name,dep,salary) VALUES(%s,%s,%s,%s)"
                depID = int(input("Enter dep ID: "))
                name = input("Enter your name: ").strip()
                depName = input("Enter department name: ").strip()
                salary = float(input("Enter your salary: "))

                val = (depID, name, depName, salary)
                cursor.execute(query, val)
                conn.commit()

                print(f"Inserted successfully: {name} in {depName}")

            except Exception as e:
                conn.rollback()
                print("Error:", str(e))

        def groupbyCallCount():
            try:
                query = "SELECT dep, COUNT(*) as department_group FROM employe GROUP BY dep"
                cursor.execute(query)
                data = cursor.fetchall()
                for d in data:
                    print(d)

            except Exception as e:
                print("Error:", str(e))

        def getByMCP():

            async def main():
                server = StdioServerParameters(
                    command="python",
                    args=["grpByMcpServer.py"]
                )

                async with stdio_client(server) as (read, write):
                    async with ClientSession(read, write) as session:

                        await session.initialize()

                        try:
                            emp_id = int(input("Enter employee Search ID: "))

                            result = await session.call_tool(
                                "getEmpData",
                                {"id": emp_id}
                            )

                            print("Info:", result.content[0].text)

                        except ValueError:
                            print("Please enter a valid numeric ID")

                        except Exception as e:
                            print("Full Error:", repr(e))

            asyncio.run(main())

        # Call MCP function
        getByMCP()

    except Exception as e:
        print("Error in handling:", str(e))

else:
    print("Connection failed")

cursor.close()
conn.close()