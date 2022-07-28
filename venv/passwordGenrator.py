#Strength of the password
import re

Password=input("Enter your password ")

if re.search("[0-9]",Password):
    print("Poor")
elif re.search("[0,9]*[a-z]*",Password):
    print("Medium")

