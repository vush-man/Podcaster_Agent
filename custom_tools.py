import os
import base64
import wave
from datetime import datetime
from google.genai import Client, types

def gemini_voice_tool(script: str) -> str:
    client = Client(api_key = os.getenv("GEMINI_API_KEY"))
    interaction = client.interactions.create(
        model = "gemini-3.1-flash-tts-preview",
        input = script,
        response_format={"type": "audio"},
        generation_config = {
            "speech_config": [
                {"speaker": "Joe", "voice": "Kore"},
                {"speaker": "Jane", "voice": "Puck"}
            ]
        }
    )
    
    audio_bytes = base64.b64decode(interaction.output_audio.data)
    
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/podcast-{datetime.now().strftime('%Y%m%d-%H%M%S')}.wav"
    
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(bytes(audio_bytes))
    
    return filename