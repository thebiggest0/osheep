import requests

# request response from model


def request_model(prompt, model):
    # send paragraph and prompt to model to interpret
    url = "https://localhost:5000"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"
