import re
import os
import base64
import wave
from datetime import datetime
from google.genai import Client
from pydub import AudioSegment
import io

def parse_segments(script_text):
    """Split script text into segments based on [SEGMENT: ...] markers."""
    parts = re.split(r'\[SEGMENT:.*?\]', script_text)
    return [p.strip() for p in parts if p.strip()]

def synthesize_chunk(client, text_chunk):
    """Call Gemini TTS with consistent Joe/Jane speaker config every time."""
    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=text_chunk,
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"speaker": "Joe", "voice": "Kore"},
                {"speaker": "Jane", "voice": "Puck"}
            ]
        }
    )
    return base64.b64decode(interaction.output_audio.data)

def pcm_to_audiosegment(pcm_bytes, channels=1, rate=24000, sample_width=2):
    """Wrap raw PCM bytes in an in-memory WAV so pydub can read it."""
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm_bytes)
    buf.seek(0)
    return AudioSegment.from_file(buf, format="wav")

def build_full_podcast(script_text, output_path=None):
    client = Client(api_key=os.getenv("GEMINI_API_KEY"))
    segments = parse_segments(script_text)
    silence = AudioSegment.silent(duration=300)
    full_audio = AudioSegment.empty()

    for i, seg in enumerate(segments):
        print(f"Synthesizing segment {i+1}/{len(segments)}...")
        pcm_bytes = synthesize_chunk(client, seg)
        segment_audio = pcm_to_audiosegment(pcm_bytes)
        full_audio += segment_audio
        if i < len(segments) - 1:
            full_audio += silence

    os.makedirs("outputs", exist_ok=True)
    if output_path is None:
        output_path = f"outputs/podcast_full-{datetime.now().strftime('%Y%m%d-%H%M%S')}.wav"

    full_audio.export(output_path, format="wav")
    print(f"Done: {output_path}")
    return output_path