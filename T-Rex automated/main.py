import pyautogui
from PIL import Image

import time


time.sleep(5)
print("Start")
locate_start = pyautogui.locateOnScreen("to_start.PNG", confidence=0.7)
if locate_start is not None:
    pyautogui.press("space")
else:
    print("Nope")
