import azure.functions as func
import logging
from openai import OpenAI

# { "prompt": "Give me the top passers in the nfl during the last decade", "temperature": 0 }

secret_key = ""

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="first_func")
def first_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )


@app.route(route="completion_api", auth_level=func.AuthLevel.ANONYMOUS)
def completion_api(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    client = OpenAI(api_key=secret_key)

    req_body = req.get_json()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": req_body["prompt"]},
        ],
        max_tokens=100,
        temperature=req_body["temperature"],
    )

    return func.HttpResponse(
        completion.choices[0].message.content,
        status_code=200,
    )


@app.route(route="image_api", auth_level=func.AuthLevel.ANONYMOUS)
def image_api(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    client = OpenAI(api_key=secret_key)

    req_body = req.get_json()

    response = client.images.generate(
        model="dall-e-3", prompt=req_body["prompt"], n=1, size="1024x1024"
    )

    image_url = response.data[0].url

    return func.HttpResponse(f"Generated image URL: {image_url}", status_code=200)
