import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from dotenv import load_dotenv

load_dotenv(r"C:\Users\hulaspet\DEV\Python_env\.env")
CHROME_DRIVER_PATH = ChromeService(executable_path=os.getenv("chrome_driver"))
LINK_TO_SITE = "https://elgoog.im/t-rex/"

class AutoJump:
    def __init__(self):
        self.obstacle_x = 0
        self.obstacle_y = 0

    def open_browser(self):
        """Opens Chrome and waits 5 seconds to load the site."""
        driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        driver.get(LINK_TO_SITE)
        driver.maximize_window()
        time.sleep(5)

    def get_coordinates(self):
        """Gets the center coordinates of the dino based on a picture
        Sets the obstacle position based on the position of the dino."""
        jump = pyautogui.locateOnScreen("to_start.PNG", confidence=0.95)
        dino_coord = pyautogui.center(jump)
        self.obstacle_x = int(dino_coord[0] * 1.20)
        self.obstacle_y = int(dino_coord[1] * 1.02)


bot = AutoJump()
bot.open_browser()
bot.get_coordinates()
pyautogui.press('up')

while True:
    jumper = pyautogui.pixelMatchesColor(bot.obstacle_x, bot.obstacle_y, expectedRGBColor=(83, 83, 83))
    if jumper:
        pyautogui.press('up')

