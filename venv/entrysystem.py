import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def entry():
    Time=int(datetime.datetime.now().hour)
    if Time>=0 and Time<12:
        speak("Good Morning Sir. You are on a morning shift.")
    if Time>=12 and Time <15:
        speak("Good Afternoon Sir .You are on mid shift.")
    if Time>=15 and Time<20:
        speak("Good Evening Sir. You are late for mid shift.")
    if Time>=20 and Time<=24:
        speak("You are doing night shift. Drink Your Coffee.")

    speak("Anything else u want to ask.I can't be able to answer because for that code is incomplete ... Sorry.")
    speak("Fuck off")
entry()
