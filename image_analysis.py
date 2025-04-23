import requests

def analyze_image(image_path: str, prompt: str) -> str:
    question = prompt or "What issue can you detect in this property image?"
    combined_prompt = f"Property Image Description: {image_path}\n\n{question}"

    response = requests.post("http://20.84.56.193:11434/api/generate", json={
        "model": "llava",
        "prompt": combined_prompt,
        "stream": False
    })

    return response.json().get("response", "No response from image model.")

