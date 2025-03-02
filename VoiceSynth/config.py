import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY_FILE = ".env"


def get_api_key():
    """Retrieve API key from the environment or prompt the user to enter it."""
    api_key = os.getenv("ELEVENLABS_API_KEY")

    if api_key:
        return api_key

    api_key = input("Enter your Eleven Labs API key: ").strip()

    with open(API_KEY_FILE, "w") as file:
        file.write(f"ELEVENLABS_API_KEY={api_key}\n")

    print("API key saved successfully!")
    return api_key
