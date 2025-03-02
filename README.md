# 🎙️ **VoiceSynth** – AI-Powered Text-to-Speech  
Turn text into **realistic AI-generated speech** with **multiple voices** using **ElevenLabs API**. 🎵

## **About VoiceSynth**  
**VoiceSynth** is an advanced **text-to-speech (TTS) generator** powered by **ElevenLabs API**. It allows users to **convert text into realistic AI-generated speech** and save it as an **MP3 file**.  

Perfect for **content creators, accessibility tools, podcasts, and voice assistants**!  

---

## **Features**  
✅ **Realistic AI-generated voices**  
✅ **20+ unique voices to choose from**  
✅ **MP3 file output for easy sharing**  
✅ **Secure API key storage using `.env`**  
✅ **Customizable voice settings (stability & similarity boost)**    

---

## **Installation**  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/nayandas69/VoiceSynth.git
cd VoiceSynth
```

### **2️⃣ Create & Activate Environment
```sh
python3 -m venv .venv  # create environment
source .venv/bin/activate  # activate environment
```

### **3️⃣ Install Dependencies**  
```sh
pip3 install -r requirements.txt
```

---

## **API Key Setup**  
1️⃣ Get an API key from **[ElevenLabs](https://elevenlabs.io/)** (free signup).  
2️⃣ Run the script, and it will **prompt** for your API key.  
3️⃣ The key is securely saved in a `.env` file.  

Alternatively, manually add the API key:  
```sh
echo "ELEVENLABS_API_KEY=your_api_key_here" > .env
```

---

## **How to Use**  
Run the main script:  
```sh
python3 voicesynth.py  # run the script
```

**Follow these steps:**  
1️⃣ **Enter text** to convert into speech.  
2️⃣ **Select a voice** from the available options.  
3️⃣ **Enter a filename** to save the audio.  
4️⃣ **Speech is generated** and saved in the `output/` folder.  

---

## **Available Voices**  
Now featuring **20+ AI-generated voices!** 🎙️  

| #  | Voice Name        | Voice ID                    |
|----|-------------------|-----------------------------|
| 1  | Sam               | `yoZ06aMxZJJ28mfd3POQ`      |
| 2  | Domi              | `AZnzlk1XvdvUeBnXmlld`      |
| 3  | Elli              | `MF3mGyEYCl7XYWbV9V6O`      |
| 4  | Josh              | `TxGEqnHWrfWFTfGW9XjX`      |
| 5  | Adam              | `pNInz6obpgDQGcFmaJgB`      |
| 6  | Emily             | `LcfcDJNUP1GQjkzn1xUU`      |
| 7  | Sarah             | `EXAVITQu4vr4xnSDxMaL`      |
| 8  | James             | `ZQe5CZNOzWyzPSCn5a3c`      |
| 9  | Niraj             | `zgqefOY5FPQ3bB7OZTVR`      |
| 10 | David             | `BNgbHR0DNeZixGQVzloa`      |
| 11 | Liang             | `FjfxJryh105iTLL4ktHB`      |
| 12 | Bella             | `EXAVITQu4vr4xnSDxMaL`      |
| 13 | Rachel            | `21m00Tcm4TlvDq8ikWAM`      |
| 14 | Antoni            | `ErXwobaYiN019PkySvjV`      |
| 15 | Arnold            | `VR6AewLTigWG4xSOukaG`      |
| 16 | Michael           | `flq6f7yk4E4fJM5XTYuZ`      |
| 17 | Vanessa           | `TpIle0udG1y9a8xmjXsn`      |
| 18 | Ishibashi         | `Mv8AjrYZCBkdsmDHNwcB`      |
| 19 | Monika Sogam      | `1qEiC6qsybMkmnNdVMbK`      |
| 20 | W. Darth Oxley    | `G3zrXA9moYrFCgwBAvxJ`      |
| 21 | Larisa Actrisa    | `AB9XsbSA4eLG12t2myjN`      |

---

## **Example Usage**
```
Enter the text you want to convert to speech: Hello! This is an AI-powered voice.
Enter the desired output file name (without extension): ai_voice

Available voices:
1. Sam
2. Domi
3. Elli
...

Enter the number corresponding to the desired voice: 3

🎙️ Generating speech...
✅ Speech saved successfully: output/ai_voice.mp3
```

---

## **Configuration & Customization**  
### **Modify Voice Stability & Similarity Boost**  
Edit the `tts.py` file:  
```python
"voice_settings": {
    "stability": 0.7,  # (0-1) Higher = more robotic, Lower = more natural
    "similarity_boost": 0.8  # (0-1) Adjusts voice consistency
}
```

### **Change Output Folder**
Modify the `tts.py` file:  
```python
OUTPUT_DIR = "your_new_folder"
```

---

## **Troubleshooting**
### API Key Not Found  
Run:  
```sh
rm -rf .env  # Delete API key file
python3 voicesynth.py  # Re-enter API key
```

### Error 401: Invalid API Key  
Ensure the **API key is correct** in `.env` or re-enter it.

### Speech Not Generated  
- Ensure **internet connectivity** is available.  
- **Try different voices** (some might be temporarily unavailable or  voice is not available for free users).  

## **License**  
This project is **open-source** under the **MIT License**.  

## **Contributing**  
🔹 Want to add new features or voices? Fork the repo and submit a PR!  
🔹 Have suggestions? Open an issue on GitHub.  

## **Support the Project!**  
If you found **VoiceSynth** useful, ⭐ **Star this repo** on GitHub! 
