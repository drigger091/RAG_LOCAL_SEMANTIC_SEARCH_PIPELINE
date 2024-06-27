import ollama

response = ollama.chat(
    model="llama3:instruct",
    messages=[
        {"role": "system", "content": "Hello, You are a helpful assistant."},
        {"role": "user", "content": "What is machine learning?"},
        {"role": "assistant", "content": "Machine Learning is a subfield of Artificial Intelligence where models learn from data."},
        {"role": "user", "content": "What is deep learning?"}
    ]
)

print(response['message']['content'])
