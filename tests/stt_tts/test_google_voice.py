import sys
import os
import pytest
from google.cloud import speech

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stt_tts.stt_google import transcribe_audio
from stt_tts.tts_google import synthesize_text

AUDIO_PATH = os.path.join(os.path.dirname(__file__), "audio/sample_audio_fixed.wav")

@pytest.mark.stt_google
def test_stt_google():
    result = transcribe_audio(AUDIO_PATH)  # ensure 16kHz .wav
    assert isinstance(result, str) and len(result) > 0
    print("Transcription:", result)

@pytest.mark.tts_google
def test_tts_google():
    output_file = synthesize_text("Hello, Wellness Hub!")
    assert os.path.exists(output_file)
    print("TTS output saved at:", output_file)