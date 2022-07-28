import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def gettime():
    return datetime.datetime.now()


def entry():
    Time=int(datetime.datetime.now().hour)
    name = input("Hello please enter your name to continue: ")
    # print(name)
    if name== "Dhiren":
        if Time>=0 and Time<12:
            speak("Good Morning Sir. You are on a morning shift.")
        if Time>=12 and Time <=20:
            speak("Good Afternoon Sir .You are on mid shift.")
    # if Time>=15 and Time<20:
    # speak("Good Evening Sir. You are late for mid shift.")
        if Time>=20 and Time<=24:
            speak("You are doing night shift. Drink Your Coffee.")
        with open("nameentryDhr.txt","a") as fileopen1:
                fileopen1.write(str([str(gettime())])+": Dhiren""\n")
        print(Time)
    elif name== "Raj":
        if Time>=0 and Time<12:
            speak("Good Morning Sir. You are on a morning shift.")
        if Time>=12 and Time <20:
            speak("Good Afternoon Sir .You are on mid shift.")
    # if Time>=15 and Time<20:
    # speak("Good Evening Sir. You are late for mid shift.")
        if Time>=20 and Time<=24:
            speak("You are doing night shift. Drink Your Coffee.")
        with open("nameentryRaj.txt","a") as fileopen1:
                fileopen1.write(str([str(gettime())])+": Raj ""\n")
        print(Time)
    elif name== "Shreyash":
        if Time>=0 and Time<12:
            speak("Good Morning Sir. You are on a morning shift.")
        if Time>=12 and Time <20:
            speak("Good Afternoon Sir .You are on mid shift.")
    # if Time>=15 and Time<20:
    # speak("Good Evening Sir. You are late for mid shift.")
        if Time>=20 and Time<=24:
            speak("You are doing night shift. Drink Your Coffee.")
        with open("nameentryMaa.txt","a") as fileopen1:
                fileopen1.write(str([str(gettime())])+": Shreyash""\n")
        print(Time)
    else :
        print("Enter correct name")    
Looper = 1  
  
while True: 
    entry()  
    Looper = int(input("Enter 1 to enter again 0 to exit"))
    if(Looper == 0):  
        break  



