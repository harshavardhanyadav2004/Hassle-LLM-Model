import requests

def answer_faq(prompt: str) -> str:
    response = requests.post("http://20.84.56.193:11434/api/generate", json={
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "No response from FAQ model.")