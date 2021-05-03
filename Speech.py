import speech_recognition as sr
 
audio = ("Generico.wav")

r = sr.Recognizer()

with sr.AudioFile(audio) as source:
    info_audio = r.record(source)
    texto = r.recognize_google(info_audio, language = "es-us" )
    print(texto)