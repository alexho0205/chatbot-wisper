# whisper demo , mp3 to transcribe
import os
import openai
openai.api_key = "OPAI_API_KEY"
audio_file = open("C:\\Users\\010940\\Downloads\\your_audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"])


