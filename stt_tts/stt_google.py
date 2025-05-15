import wave
import io
from google.cloud import speech

def get_sample_rate(path):
    with wave.open(path, 'rb') as wf:
        return wf.getframerate()

def transcribe_audio(path):
    client = speech.SpeechClient()
    
    sample_rate = get_sample_rate(path)

    with io.open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = [result.alternatives[0].transcript for result in response.results]
    return " ".join(transcripts)