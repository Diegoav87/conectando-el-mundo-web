from openai import OpenAI

secret_key = ""

prompt = "Give me the top passers in the nfl during the last decade"

client = OpenAI(api_key=secret_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=100,
    temperature=0,
)

print(completion.choices[0].message.content)
