import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import pywhatkit
import playsound
from pygame import mixer
# error in mixer module slove





engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<17:
        speak("Good AfterNoon Sir!")
    elif hour>=17 and hour<20:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir! Sleep Well .")

    speak("How may i help u.")
def takeCommand():
    '''
    IT take microphone input from the user and return string as output
    :return:
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said : (query)\n")
    except Exception as e:
        print(e)

        speak("Can't understand . Can you repeat it sir")
        return "None"
    return query
wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching wikipedia ...")
        query = query.replace("wikipedia","")
        results=wikipedia.summary(query,sentence=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open Youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open Google' in query:
        speak("Sir, what would you like to search .")
        cm=takecommand().lower()
        webbrowser.open(f"{cm}")


    elif 'play music ' in query:
        music_dir="C:\\Users\\ranes\\Downloads "
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        strTime=datetime.datetime.now().strtime("%H:%H:%S")
        speak(f"Sir the time is {strTime}")

    # for opening pycharm
    elif 'open pycharm' in query:
        pycharmPath="C:\\Program\\Files\\JetBrains\\PyCharm\\Community\\Edition\\2021.1.1\\bin\\pycharm64.exe"
        os.startfile(pycharmPath)

    # Work is remaning in this.
    elif "send message" in query:
        speak("Whom would u like to sent the message sir?")
        speak("Can u tell me the number.")
        number=takeCommand()
        pywhatkit.sendwhatmsg()

    # play song on youtube
    elif "play song on youtube" in query:
        speak("Which song would you like to hear sir?")
        song=takeCommand().lower()
        pywhatkit.playonyt(f"{song}")
    # for Spotify
    elif "open Spotify" in query:
        spotifyPath="C:\\Users\\ranes\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(spotifyPath)

    #for predator sense
    elif "open predator sense" in query:
        speak("Opening Predator sense sir")
        predatorSensePath="C:\\Program Files (x86)\\Acer\\PredatorSense\\PredatorSense.exe"
        os.startfile(predatorSensePath)

    #for alarm (Work in progrees)
    elif "alarm" in query:
        speak("At what time the alarm should ring sir .")
        time=takeCommand().isdigit()

        while True:
            Time_Ac = datetime.datetime.now()
            now=Time_Ac.strftime("%H:%M:%S")

            if now == Time:
                speak("Time to Wake up Sir!")
                mixer.music.load('Bazanji Fed Up .mp3')
                if "Stop alarm" in query:
                    speak("As your wish sir.")
                    mixer.music.stop()


            elif now > Time:
                break

    #for reminding something
    elif "remeber that" in query:
        rememberMsg=query.replace("remember that","")
        rememberMsg=rememberMsg.replace("Jarvis","")
        speak("You tell me to remind you that : "+rememberMsg)
        remember =open("data.txt","w")
        remember.write(rememberMsg)
        remember.close()

    elif " what do you remember " in query:
        remember=open("data.txt","r")
        speak("You have told me to remember that "+remember)











