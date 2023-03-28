import openai
import config
import pyaudio
import wave
from gtts import gTTS
import os
# from pydub import AudioSegment

openai.api_key = config.OPENAI_API_KEY

chats = []

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )

    message = completions.choices[0].text
    return message.strip()

def generate_audio(text):
    tts = gTTS(text, lang='en')
    tts.save('audio.mp3')
    with open('audio.mp3', 'rb') as f:
        audio_content = f.read()
    os.remove('audio.mp3')
    return audio_content

def transcribe(audio):
  audio_file = open(audio, "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file,language = "en", response_format="json")
  return transcript.text

    
# resp = generate_response("give me an example of a prompt i could use to ask a user for their medication")
# chats.append({"role":"assistant", "content":resp})

# def tts(txt, name):
#   myobj = gTTS(text=txt, lang="en", slow=False)
#   sound_file = name
#   myobj.save(sound_file)

# tts(resp,'tts.wav')

# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 2
# fs = 44100  # Record at 44100 samples per second
# seconds = 60
# filename = "output.wav"

# p = pyaudio.PyAudio()  # Create an interface to PortAudio

# print('Recording')

# stream = p.open(format=sample_format,
#                 channels=channels,
#                 rate=fs,
#                 frames_per_buffer=chunk,
#                 input=True)
 
# frames = []  # Initialize array to store frames

# # Store data in chunks for x seconds
# # for i in range(0, int(fs / chunk * seconds)):
# #     data = stream.read(chunk)
# #     frames.append(data)

# try:
#   while True:
#     data = stream.read(chunk)
#     frames.append(data)
# except KeyboardInterrupt:
#   pass

# # Stop and close the stream 
# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()

# print('Finished recording')

# # Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()

# stt = transcribe("output.wav")
# print(stt)

# chats.append({"role":"user", "content":stt})

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=chats
# )
# msg = completion.choices[0].message.content.strip()
# tts(msg, 'tts2.wav')