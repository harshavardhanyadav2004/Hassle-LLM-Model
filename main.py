from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from image_analysis import analyze_image
from tenancy_faq import answer_faq

app = FastAPI()

@app.post("/chat")
async def chat( prompt: str = Form(...), file: Optional[UploadFile] = File(None)):
    if file is not None:
        image_path = f"/tmp/{file.filename}"
        with open(image_path, "wb") as f:
            f.write(await file.read())
        result = analyze_image(image_path, prompt)
        return {"agent": "Issue Detection Agent", "response": result}

    result = answer_faq(prompt)
    return {"agent": "Tenancy FAQ Agent", "response": result}
