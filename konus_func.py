from playsound import playsound
from gtts import gTTS #google'a bağlanma
from googletrans import Translator 
import os

def konus(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file ="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
