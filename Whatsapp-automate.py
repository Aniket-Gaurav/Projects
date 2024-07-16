import pyautogui as pg
import time

time.sleep(5)

for i in range(20):
    pg.write("You are not Texting me now...")
    time.sleep(0.5)
    pg.press("Enter")