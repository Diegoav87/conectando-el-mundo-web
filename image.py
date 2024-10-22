from openai import OpenAI

secret_key = ""

prompt = "The baker mayfield led cleveland browns winning the super bowl"

client = OpenAI(api_key=secret_key)


response = client.images.generate(
    model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
)

# Get the image URL from the response
image_url = response.data[0].url
print(f"Generated image URL: {image_url}")
