# 最终稿：

import gradio as gr
import openai, subprocess
from pydub import AudioSegment

openai.api_key = "OPAI_API_KEY"
messages = [{"role": "system", "content": '你是一名知識淵博，樂於助人的智能聊天機器人.你的任務是陪我聊天，請用簡短的對話方式，用中文講一段話，每次回答不超過50個字！'}]

def transcribe(audio):
    global messages

    # convert wav to mp3
    # audio is full file path
    mp3_file = audio+".mp3";
    pcm_file = AudioSegment.from_wav( audio )
    pcm_file.export( mp3_file , format="mp3")

    audio_file = open(mp3_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    subprocess.call(["wsay", system_message['content']])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()