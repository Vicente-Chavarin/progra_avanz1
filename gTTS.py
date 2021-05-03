from gtts import gTTS
tts = gTTS("Este texto se convertira en audio y el audio en texto", lang ="es-us")
tts.save("Generico.wav")
#with open("2_hola_mundo.mp3", "wb") as archivo:
 #    tts.write_to_fp(archivo)