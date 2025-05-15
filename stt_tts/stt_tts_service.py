from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from stt_tts.stt_google import transcribe_audio
from stt_tts.tts_google import synthesize_text
import shutil
import os
import uuid

app = FastAPI(title="Wellness Hub Voice API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/api/stt")
async def stt_transcription(audio: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{audio.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
    
    try:
        transcript = transcribe_audio(file_path)
        return {"transcript": transcript}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/api/tts")
async def tts_synthesis(text: str = Form(...)):
    try:
        output_path = synthesize_text(text)
        return FileResponse(output_path, media_type="audio/mpeg", filename="output.mp3")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})