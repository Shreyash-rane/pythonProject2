import random
import pyttsx3
import re

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


digits="0123456789"
Password2="abcdefghijklmnopqrstuvwxyz0123456789"
Password3="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
Password4="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*_+-|/"

Length_Of_Password=int(input("Enter length of password : "))
print("Enter 1 for password containing only digits.")
speak("Enter 1 for password containing only digits.")
print("Enter 2 for password containing digits and lowercase.")
speak("Enter 2 for password containing digits and lowercase")
print("Enter 3 for password containing digits, lowercase and  uppercase.")
speak("Enter 3 for password containing digits, lowercase and  uppercase.")
print("Enter 4 for password containing digits,lowercase,uppercase and specialcharacter.")
speak("Enter 4 for password containing digits,lowercase,uppercase and specialcharacter.")

Password_Type=int(input("Enter Your Password Type : "))

if Password_Type == 1:
    a="".join(random.sample(digits,Length_Of_Password))
    speak("Your password is : ")
    print(a)
elif Password_Type == 2:
    a="".join(random.sample(Password2,Length_Of_Password))
    speak("Your password is :")
    print(a)
elif Password_Type == 3:
    a="".join(random.sample(Password3,Length_Of_Password))
    speak("Your password is : ")
    print(a)
elif Password_Type == 4:
    a="".join(random.sample(Password4,Length_Of_Password))
    speak("Your password is : ")
    print(a)
else:
    print("Enter a valid number.")


#Check Your PAssword Strength
speak("For checking your password strength .")
print("For checking password strength . ")

Password=int(input("Enter your password."))


