import random
import pyautogui
import string

character = string.printable #IT take all the value with which password can make.
character_list=list(character)
password = pyautogui.password("Enter password here ")

o="No"

guess_password=""
while guess_password!=password:
    guess_password=random.choices(character_list,k=len(password))
    print("////////"+str(guess_password)+"////////")
    if  guess_password == list(password):
        print("Your passwd is : "+ "".join(guess_password))
        break



