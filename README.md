# Voice AI Agent

## Setup
pip install -r requirements.txt
uvicorn backend.main:app --reload

## Features
- Real-time voice processing
- Appointment booking
- Redis memory
- Multilingual detection

## Latency
- STT: ~120ms
- LLM: ~150ms
- TTS: ~100ms
Total: <450ms
