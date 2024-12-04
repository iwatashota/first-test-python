from openai import OpenAI

openai = OpenAI(api_key="sk-proj-66666666666666666666666666666666")

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the weather in Tokyo?"}]
)

print(response)