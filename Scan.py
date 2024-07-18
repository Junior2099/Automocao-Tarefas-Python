import pyautogui
import time
import sys

pyautogui.press("win")
time.sleep(1)
pyautogui.write("ESCANER CANON")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.click(x=881, y=491)
time.sleep(1)
sys.exit(0) 