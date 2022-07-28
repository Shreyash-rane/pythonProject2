import pyautogui
o="NO"
while o == "NO":
  o=pyautogui.confirm("Have you clicked inside text box where u wanted to type ?",buttons = ["Yes","No"])
for i in range(1,50):
  pyautogui.write("Fook off",interval=0.1)
  pyautogui.press("Enter")