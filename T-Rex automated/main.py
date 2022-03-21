import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from dotenv import load_dotenv

load_dotenv(r"C:\Users\hulaspet\DEV\Python_env\.env")
CHROME_DRIVER_PATH = ChromeService(executable_path=os.getenv("chrome_driver"))
LINK_TO_SITE = "https://elgoog.im/t-rex/"

driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.get(LINK_TO_SITE)
driver.maximize_window()

time.sleep(5)
pyautogui.press('up')
while True:
    #1st way
    # jump = pyautogui.locateOnScreen("not_clear.PNG", confidence=0.95)
    # if jump == None:
    #     pyautogui.press("up")
    #2nd way
    jumper = pyautogui.pixelMatchesColor(720, 550, (83, 83, 83))
    if jumper:
        pyautogui.press('up')

