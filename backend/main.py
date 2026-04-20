from fastapi import FastAPI, WebSocket
from agent.orchestrator import process_input
from services.stt import speech_to_text
from services.tts import text_to_speech
import time

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    while True:
        start = time.time()

        audio = await ws.receive_bytes()

        text = speech_to_text(audio)
        response_text = process_input(text)
        audio_out = text_to_speech(response_text)

        latency = time.time() - start
        print(f"Latency: {latency:.3f}s")

        await ws.send_bytes(audio_out)
