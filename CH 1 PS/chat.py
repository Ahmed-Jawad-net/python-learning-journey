from openai import OpenAI

client = OpenAI(api_key="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")  # Your actual API key here

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)

print(response.choices[0].message.content)