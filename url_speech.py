import requests
import io
import speech_recognition as sr
from pydub import AudioSegment


# This function translate speech to text
def speech_to_text(file):
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(file)
    with audio as source:
        speech = recognizer.record(source)
        try:
            # Call recognizer with audio and language
            text = recognizer.recognize_google(speech, language='pt-BR')
            print("Você disse: " + text)
            return text
        # If recognizer don't understand
        except:
            print("Não entendi")

def mp4_to_wav(file):
    audio = AudioSegment.from_file(file, format="mp4")
    audio.export("audio.wav", format="wav")
    return audio

def mp4_to_wav_mem(file):
    print('Converting wav file into wav')
    audio = AudioSegment.from_file_using_temporary_files(file, 'mp4')
    file = io.BytesIO()
    file = audio.export(file, format="wav")
    file.seek(0)
    print('Audio file conversed to wav')
    return file

def ogg_to_wav(file):
    print('Converting ogg file into wav')
    audio = AudioSegment.from_file_using_temporary_files(file, 'ogg')
    file = io.BytesIO()
    file = audio.export(file, format="wav")
    file.seek(0)
    print('Audio file conversed to wav')
    return file

url = 'https://cdn.fbsbx.com/v/t59.3654-21/75487881_3284647991576849_1113266638498562048_n.mp4/audioclip-1576251271-3762.mp4?_nc_cat=103&_nc_ohc=OAA4kYBlJVEAQn3xqdgBfpT7oyAXCHYK1XtI6bA1rdId0Ow_1PrgVWDAQ&_nc_ipfwd=1&_nc_ht=cdn.fbsbx.com&oh=566dc46d8909bd71b23dfe59f8601199&oe=5DF5B268'
r = requests.get(url, stream=True)
file = io.BytesIO(r.content)
file = mp4_to_wav_mem(file)
speech_to_text(file)
