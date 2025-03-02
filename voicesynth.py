from voicesynth.utils import get_text, get_output_filename
from voicesynth.voices import select_voice
from voicesynth.tts import generate_speech


def main():
    """Main function to run the speech synthesis program."""
    text = get_text()
    voice_id = select_voice()
    output_filename = get_output_filename()
    generate_speech(text, voice_id, output_filename)


if __name__ == "__main__":
    main()
