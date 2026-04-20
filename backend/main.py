from fastapi import FastAPI, WebSocket
from agent.orchestrator import process_input
from services.stt import speech_to_text
from services.tts import text_to_speech
import time

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

# ✅ TEST ENDPOINT (VERY IMPORTANT FOR DEMO)
@app.get("/test")
def test():
    return {"response": process_input("book appointment tomorrow")}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    
    while True:
        start = time.time()
        
        data = await ws.receive()

        # ✅ Supports BOTH text & audio
        if "text" in data:
            text = data["text"]
        else:
            text = speech_to_text(data["bytes"])
        
        response_text = process_input(text)
        audio_out = text_to_speech(response_text)
        
        latency = time.time() - start
        print({"latency": latency})
        
        await ws.send_text(response_text)
