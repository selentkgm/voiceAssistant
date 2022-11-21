from distutils.text_file import TextFile
from email.mime import audio
from playsound import playsound
from gtts import gTTS #google'a bağlanma
import speech_recognition as sr
from googletrans import Translator 
import os
import time
import webbrowser
from konus_func import konus

r = sr.Recognizer()

def kaydet(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
            print(voice)
        except sr.UnknownValueError:
            print("Asistan: Anlamadım ")
            konus("Anlamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
            konus("Sistem çalışmıyor")
        return voice 
