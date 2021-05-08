import pyautogui, time
from colorama import init
from colorama import Fore, Back, Style

# Use init()
init()

# text coloring
print( Fore.GREEN )
print( Back.BLACK )
print( Style.BRIGHT )
print("You have 5 second for start spam!!!")

# start delay
time.sleep(5)

# Launching
f = open("Text.txt", "r")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")