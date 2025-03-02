def get_text():
    """Prompt user for input text."""
    return input("\nEnter the text you want to convert to speech: ").strip()


def get_output_filename():
    """Prompt user for the output filename."""
    return input("Enter the desired output file name (without extension): ").strip()
