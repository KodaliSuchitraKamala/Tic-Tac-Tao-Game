import pyautogui as pg
import time
import random

animals = ['dog','monkey','donkey','pig']

time.sleep(10)

for i in range(20):
    a=random.choice(animals)
    pg.write(f"you are a {a}")
    pg.press('enter')