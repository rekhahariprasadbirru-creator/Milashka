
import asyncio
import edge_tts

async def speak(text):
    voice = "hi-IN-SwaraNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("milashka.mp3")

if __name__ == "__main__":
    asyncio.run(speak("Namaste! Main Milashka hoon."))
