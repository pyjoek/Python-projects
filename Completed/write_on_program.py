import random

#@python.code_

import pyautogui as pg
import time

animal = ("programming", "hacking")
time.sleep(8)

for i in range(100):
	a = random.choice(animal)
	pg.write("i am " + a)
	pg.press("enter")
