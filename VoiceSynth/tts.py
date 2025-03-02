import os
import requests
from voicesynth.config import get_api_key

# API Configuration
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

# Ensure output directory exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_speech(text, voice_id, output_filename):
    """Send request to Eleven Labs API and generate speech."""
    api_key = get_api_key()

    headers = {
        "accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.6,  # Adjust voice stability (0-1)
            "similarity_boost": 0.7,  # Adjust naturalness (0-1)
        },
    }

    print("\nGenerating speech...")

    response = requests.post(
        f"{API_URL}/{voice_id}?optimize_streaming_latency=0",
        headers=headers,
        json=payload,
    )

    if response.status_code == 200:
        file_path = os.path.join(OUTPUT_DIR, f"{output_filename}.mp3")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Speech saved successfully: {file_path}")
    else:
        print(f"Error {response.status_code}: {response.text}")
