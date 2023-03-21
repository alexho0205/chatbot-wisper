
# 测试3， WHISPER API

import gradio as gr
import openai
from pydub import AudioSegment

openai.api_key = "OPAI_API_KEY"

def transcribe(audio):
    #print(audio)

    # convert wav to mp3
    # audio is full file path
    mp3_file = audio+".mp3";
    pcm_file = AudioSegment.from_wav( audio )
    pcm_file.export( mp3_file , format="mp3")

    audio_file= open(mp3_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

ui = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text"
).launch()

ui.launch()