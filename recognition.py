import speech_recognition as sr


r = sr.Recognizer() 
 
with sr.Microphone() as source:
    print('Speak Anything : ')
    info_audio = r.listen(source)
 
    try:
        text = r.recognize_google(info_audio, language = "es-us")
        print('You said: {}'.format(text))
    except:
        print('Sorry could not hear')