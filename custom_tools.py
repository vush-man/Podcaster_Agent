import os
import base64
import wave
from datetime import datetime
from google.genai import Client, types

def gemini_voice_tool(script: str) -> str:
    client = Client(api_key = os.getenv("GEMINI_API_KEY_2") or os.getenv("GOOGLE_API_KEY_2"))
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash-preview-tts",
        contents = script,
        config = types.GenerateContentConfig(
            response_modalities = ["AUDIO"],
            speech_config = types.SpeechConfig(
                multi_speaker_voice_config = types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs = [
                        types.SpeakerVoiceConfig(
                            speaker = 'Joe',
                            voice_config = types.VoiceConfig(
                                prebuilt_voice_config = types.PrebuiltVoiceConfig(voice_name='Orus')
                            )
                        ),
                        types.SpeakerVoiceConfig(
                            speaker = 'Jane',
                            voice_config = types.VoiceConfig(
                                prebuilt_voice_config = types.PrebuiltVoiceConfig(voice_name='Leda')
                            )
                        ),
                    ]
                )
            )
        )
    )
    
    audio_bytes = response.candidates[0].content.parts[0].inline_data.data
    if isinstance(audio_bytes, str):
        audio_bytes = base64.b64decode(audio_bytes)
    
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/podcast-{datetime.now().strftime('%Y%m%d-%H%M%S')}.wav"
    
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(bytes(audio_bytes))
    
    return filename