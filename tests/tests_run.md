
# 🧪 Running Tests for Wellness Hub

This guide explains how to run all test cases across the Wellness Hub project.

---

## 📦 1. Install All Dependencies

Make sure your virtual environment is active.

```bash
python -m venv venv
source venv/bin/activate  # or `source venv/bin/activate.fish` for fish shell
pip install -r requirements.txt
```

---

## 🛠️ 2. Set `PYTHONPATH`

To ensure internal modules like `stt_tts` resolve correctly:

```bash
export PYTHONPATH=.
```

For Zsh or Fish shell:

```bash
export PYTHONPATH=$(pwd)
```

---

## 🗂️ 3. Project Directory Structure

Make sure your folder looks like this:

```
wellness_hub/
│
├── stt_tts/
│   ├── __init__.py
│   ├── stt_google.py
│   ├── tts_google.py
│   └── stt_tts_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_google_voice.py
│   ├── test_main.py
│   ├── test_music.py
│   └── test_scheduler.py
|   |__ test_stt_tts_service_api.py
│
├── requirements.txt
└── sample_audio_fixed.wav (Mono, 16000Hz)
```

---

## 🔉 4. Ensure Audio File Format

The file `sample_audio_fixed.wav` must be:
- Mono channel
- 16000Hz sample rate
- PCM 16-bit

Use this command if needed:

```bash
ffmpeg -i tests/sample_audio.wav -ac 1 -ar 16000 tests/sample_audio_fixed.wav
```

---

## ✅ 5. Run All Tests

```bash
pytest
```

To run a specific test file (e.g., Google STT & TTS):

```bash
pytest tests/test_google_voice.py
```

You should see output like:

```
Transcription: hello welcome to wellness hub
TTS output saved at: output.mp3
```

---

## ⚙️ 6. Pytest Configuration (`pytest.ini`)

Ensure you have a `pytest.ini` file in your root folder:

```ini
[pytest]
markers =
    play_shiva: test music using playsound
    play_pygame: test music using pygame
    parse_workflow: test workflow parsing
addopts = -s --disable-warnings
testpaths = tests
python_files = test_*.py
pythonpath = .
```

---

## 🧪 Optional: Re-run Failed Tests Only

```bash
pytest --lf
```

---

## 🚀 Run API Server (Optional)

To test the STT/TTS API endpoints via FastAPI:

```bash
uvicorn stt_tts.stt_tts_service:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

To run against Google STT & TTS HTTP Server:

```bash
pytest tests/test_stt_tts_service_api.py
```

or

```bash
 PYTHONPATH=. pytest tests/test_stt_tts_service_api.py
``` 

Happy testing! 🧘‍♂️✨
