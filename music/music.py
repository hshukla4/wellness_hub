# FastAPI server (main.py)
from fastapi import FastAPI, Request
from pydantic import BaseModel
from music_player import play_shiva_music

app = FastAPI()

class BhajanRequest(BaseModel):
    bhajan_name: str

@app.post("/api/play_bhajan")
async def play_bhajan(data: BhajanRequest):
    file_map = {
        "Shiv Bhajan": "./music/om_namah_shivaya.mp3",
        "Om Namah Shivaya Chanting": "./music/om_namah_shivaya_chanting.mp3"
    }
    file_path = file_map.get(data.bhajan_name)
    if not file_path:
        return {"error": "Invalid bhajan name"}

    play_shiva_music(file_path)
    return {"message": f"Playing {data.bhajan_name}"}

