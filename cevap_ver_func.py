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
from kaydet_func import kaydet
from diller import diller

def cevapVer(voice):
    if "merhaba" in voice:
        konus.konus("sana da merhaba") #verisyon hatası verdi. playsound'un verisyonunu 1.2.2 yaparak sorun çözüldü.
    if "selam" in voice:
        konus("sana da selam ")
    if "teşekkürler" in voice:
        konus("rica ederim") 
    if "iyi geceler" in voice:
        konus("iyi geceler ")
    if "görüşürüz" in voice:
        konus("görüşürüz ")   
    if "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Sunday":
            today = "Pazar"   
        elif today == "Monday":
            today = "Pazartesi"
        elif today == "Tuesday":
            today = "Salı"
        elif today == "Wednesday":
            today = "Çarşamba"
        elif today == "Thursday":
            today = "Perşembe"
        elif today == "Friday":
            today = "Cuma"
        elif today == "Saturday":
            today = "Cumartesi"     
        konus(today)   

    if "google" in voice:
        konus("ne aramamı istersin")
        search = kaydet()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        konus("{} içi Google'da bulabildiklerimi listeledim".format(search))

    if "not et" in voice:
        konus("dosya ismi ne olsun ")
        txtFile = kaydet() + ".txt"
        konus("ne kaydetmek istersin")
        theText = kaydet()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()

    if "çevir" in voice:
        def translateEt():
            print("Çevirmemi istediğin dili söyleyin")
            print()
            to_lang = kaydet()
            while (to_lang == "None"):
                to_lang = kaydet()
            to_lang = to_lang.lower()
            return to_lang
        
        to_lang = translateEt()
        
        while (to_lang not in diller):
            print("Dil bulunamadı lütfen başka bir dil girin")
            print()
            to_lang = translateEt()
        
        to_lang = diller[diller.index(to_lang)+1]
        
        translator = Translator()
        print(to_lang)
        query = kaydet()  
        
        text_to_translate = translator.translate(query, dest=to_lang)          

        text = text_to_translate.text
        
        speak = gTTS(text=text, lang=to_lang, slow=False)
          
        speak.save("captured_voice.mp3")
          
        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')

