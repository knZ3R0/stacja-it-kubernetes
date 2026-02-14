from celery import Celery
from celery import current_task
import base64
from pathlib import Path
from transformers import pipeline

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

# Ładowanie modelu ASR Whisper Tiny
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny"
)

DATA_DIR = Path("/data")
AUDIO_DIR = DATA_DIR / "audio"
RESULTS_DIR = DATA_DIR / "results"

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

@celery.task(name="tasks.transcribe_audio")
def transcribe_audio(audio_b64: str):
    task_id = getattr(current_task.request, "id", None) or "manual-task"
    audio_bytes = base64.b64decode(audio_b64)
    audio_path = AUDIO_DIR / f"{task_id}.wav"
    audio_path.write_bytes(audio_bytes)

    result = transcriber(str(audio_path), return_timestamps=True)
    text = result["text"]

    result_path = RESULTS_DIR / f"{task_id}.txt"
    result_path.write_text(text, encoding="utf-8")

    return text