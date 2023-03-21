
# 测试3， WHISPER API

import gradio as gr
import openai
import io
import tempfile
import os
from pydub import AudioSegment

openai.api_key = "OPAI_API_KEY"

def transcribe(audio_file):

    
    

    mp3_file= open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", mp3_file)
    return transcript["text"]

ui = gr.Interface(
    fn=transcribe,
    inputs=gr.inputs.Audio(label="上傳一個聲音檔案" ,  type="filepath"),
    outputs="text"
).launch()

ui.launch()