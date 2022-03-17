#https://elgoog.im/t-rex/
import pyautogui
from PIL import Image

import time


time.sleep(5)
print("Start")
while True:
    jump = pyautogui.locateOnScreen("not_clear.PNG", confidence=0.95)
    if jump == None:
        pyautogui.press("space")

