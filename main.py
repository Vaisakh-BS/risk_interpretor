from fastapi import FastAPI, UploadFile, File
from utils.parser import extract_text_from_pdf
from utils.prompt_builder import build_risk_prompt
from llm.engine import analyze_text_with_llm
import json
app = FastAPI()

@app.post("/analyze_sop/")
async def analyze_sop(file: UploadFile = File(...)):
    file_bytes = await file.read()  # ✅ READ ONLY ONCE
    if not file_bytes:
        return {"error": "Empty or unreadable file uploaded."}

    text = extract_text_from_pdf(file_bytes)
    prompt = build_risk_prompt(text)
    import json

    raw_output = analyze_text_with_llm(prompt)

    try:
        parsed_output = json.loads(raw_output)
        return {"analysis": parsed_output}
    except json.JSONDecodeError:
        return {
        "error": "LLM returned invalid JSON",
        "raw_output": raw_output
    }
    
