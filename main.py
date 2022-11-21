from konus_func import konus
from kaydet_func import kaydet
from cevap_ver_func import cevapVer

konus("Selam") 

while True:   
   voice = kaydet()
   if voice != '':
       voice = voice.lower()
       print(voice)
       cevapVer(voice)
