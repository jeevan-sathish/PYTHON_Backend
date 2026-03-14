import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Explain machine learning in 3 lines"}
    ]
)

print(response["message"]["content"])