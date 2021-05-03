from gtts import gTTS
import playsound as playsound
import speech_recognition as sr

Texto = input("Escribe un texto que guardar en audio: ")
tts = gTTS(Texto , lang = "es-us")
Save = input("Eliga el nombre para guardad + .wav: ")
tts.save(Save)
#audio = open(Save)
#playsound = (Save)
#playsound = Save.play
#playsound(Save)