from flask import Flask,request,jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotend()

app =Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv(GROQ_API))

@app.route('/data/<int:id>',methods=["PUT"])
def handleData(id):
    response =client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":"what is rag"}
        ]

)
    return jsonify({
        "answer":response.choices[0].message.content
    })

    array =[10,20,30,40]
    data =[
        {
            "name":"jeevan",
            "age":22

        },
        {
            "name":"suhas",
            "age":23

        }
    ]

    info =request.get_json()
    name =info.get("name")
    age=info.get("age")
    details ={
        "name":name,
        "age":age
    }





    return jsonify({
        "array":array,
        "data":data,
        "details":details,
        "message":f"user {id} updated"
    })

if __name__ =="__main__":
    app.run(debug=True)