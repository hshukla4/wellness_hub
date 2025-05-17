from fastapi import FastAPI
from pydantic import BaseModel
from music.music_player import play_shiva_music

app = FastAPI()

from fastapi.staticfiles import StaticFiles

app.mount("/music", StaticFiles(directory="music/.music"), name="music")

class BhajanRequest(BaseModel):
    bhajan_name: str

@app.post("/api/play_bhajan")
async def play_bhajan(data: BhajanRequest):
    file_map = {
        "Shiv Bhajan": "./music/.music/om_namah_shivaya.mp3",
        "Om Namah Shivaya Chanting": "./music/.music/om_namah_shivaya_chanting.mp3"
    }

    file_path = file_map.get(data.bhajan_name)
    if not file_path:
        return {"status": "error", "message": "Invalid bhajan name"}

    play_shiva_music(file_path)
    return {"status": "success", "message": f"Playing {data.bhajan_name}"}