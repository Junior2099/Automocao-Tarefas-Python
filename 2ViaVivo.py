import pyautogui
import time
import sys

pyautogui.press("win")
time.sleep(1)
pyautogui.write("google")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.click(x=498, y=65)
pyautogui.write("https://login.vivo.com.br/loginmarca/appmanager/marca/publicoNovoLogin")
time.sleep(1.8)
pyautogui.press("enter")
time.sleep(8.5)
pyautogui.click(x=554, y=524)
time.sleep(1.2)
sys.exit(0) 