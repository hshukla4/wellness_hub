import sys
import requests
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

BASE_URL = "http://127.0.0.1:8000"

def test_stt_endpoint():
    audio_file = {'audio': open("tests/stt_tts/audio/sample_audio_fixed.wav", 'rb')}
    
    response = requests.post(f"{BASE_URL}/api/stt", files=audio_file)
    assert response.status_code == 200
    print("🎤 Transcription:", response.json().get("transcript"))

def test_tts_endpoint():
    text = {"text": "Welcome to the Wellness Hub!"}
    response = requests.post(f"{BASE_URL}/api/tts", data=text)
    assert response.status_code == 200
    with open("output_test.mp3", "wb") as f:
        f.write(response.content)
    print("🔊 TTS output saved to output_test.mp3")

if __name__ == "__main__":
    test_stt_endpoint()
    test_tts_endpoint()