# -*- coding: utf-8 -*-
import requests
import io
import logging as log
import speech_recognition as sr
from pydub import AudioSegment


class Speech:

    def __init__(self, source):
        self.source = source

    def process(self, url):
        text = None
        file = self.download_from_url(url)
        if file:
            if self.source == 'messenger':
                file = self.to_wav(io.BytesIO(file), 'mp4')
                text = self.speech_to_text(file)
            elif self.source == 'whatsapp':
                file = self.to_wav(io.BytesIO(file), 'ogg')
                text = self.speech_to_text(file)
        return text

    def download_from_url(self, url):
        response = requests.get(url)
        return response.content

    def to_wav(self, file, extesion):
        """ This method try to handle multiple extesions to wav on memory """
        log.info('Converting {} file into wav'.format(extesion))
        audio = AudioSegment.from_file_using_temporary_files(file, extesion)
        file = io.BytesIO()
        file = audio.export(file, format="wav")
        file.seek(0)
        log.info('Audio file conversed to wav')
        return file

    def speech_to_text(self, file):
        """ This method translates speech to text """
        recognizer = sr.Recognizer()
        audio = sr.AudioFile(file)
        log.info('Trying to convert audio into text')
        with audio as source:
            speech = recognizer.record(source)
            try:
                # Call recognizer with audio and language
                text = recognizer.recognize_google(speech, language='pt-BR')
                log.info('Text recognized: ' + text)
                return text
            # If recognizer don't understand
            except Exception:
                log.info("Speech don't understood")
                return '[Audio] Não entendi'
