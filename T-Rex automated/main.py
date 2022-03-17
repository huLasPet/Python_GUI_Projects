#https://elgoog.im/t-rex/
import pyautogui
from PIL import Image

import time


time.sleep(5)
print("Start")
while True:
    #1st way
    # jump = pyautogui.locateOnScreen("not_clear.PNG", confidence=0.95)
    # if jump == None:
    #     pyautogui.press("space")
    #2nd way
    jumper = pyautogui.pixelMatchesColor(820, 398, (83, 83, 83))
    if jumper:
        pyautogui.press('space')

