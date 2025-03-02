# List of available voices from ElevenLabs API
VOICES = [
    {"voice_id": "yoZ06aMxZJJ28mfd3POQ", "name": "Sam"},
    {"voice_id": "AZnzlk1XvdvUeBnXmlld", "name": "Domi"},
    {"voice_id": "MF3mGyEYCl7XYWbV9V6O", "name": "Elli"},
    {"voice_id": "TxGEqnHWrfWFTfGW9XjX", "name": "Josh"},
    {"voice_id": "pNInz6obpgDQGcFmaJgB", "name": "Adam"},
    {"voice_id": "LcfcDJNUP1GQjkzn1xUU", "name": "Emily"},
    {"voice_id": "EXAVITQu4vr4xnSDxMaL", "name": "Sarah"},
    {"voice_id": "ZQe5CZNOzWyzPSCn5a3c", "name": "James"},
    {"voice_id": "zgqefOY5FPQ3bB7OZTVR", "name": "Niraj"},
    {"voice_id": "BNgbHR0DNeZixGQVzloa", "name": "David"},
    {"voice_id": "FjfxJryh105iTLL4ktHB", "name": "Liang"},
    {"voice_id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella"},
    {"voice_id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel"},
    {"voice_id": "ErXwobaYiN019PkySvjV", "name": "Antoni"},
    {"voice_id": "VR6AewLTigWG4xSOukaG", "name": "Arnold"},
    {"voice_id": "flq6f7yk4E4fJM5XTYuZ", "name": "Michael"},
    {"voice_id": "TpIle0udG1y9a8xmjXsn", "name": "Vanessa"},
    {"voice_id": "Mv8AjrYZCBkdsmDHNwcB", "name": "Ishibashi"},
    {"voice_id": "1qEiC6qsybMkmnNdVMbK", "name": "Monika Sogam"},
    {"voice_id": "G3zrXA9moYrFCgwBAvxJ", "name": "W. Darth Oxley"},
    {"voice_id": "AB9XsbSA4eLG12t2myjN", "name": "Larisa Actrisa"},
    # Add more voices as needed...
]


def select_voice():
    """Prompt user to select a voice."""
    print("\nAvailable voices:")
    for index, voice in enumerate(VOICES):
        print(f"{index+1}. {voice['name']}")

    while True:
        try:
            choice = (
                int(input("\nEnter the number corresponding to the desired voice: "))
                - 1
            )
            if 0 <= choice < len(VOICES):
                return VOICES[choice]["voice_id"]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Please enter a valid number.")
