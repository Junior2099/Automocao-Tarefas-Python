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
pyautogui.write("https://portalhome.eneldistribuicaosp.com.br/#/autenticacao/login")
time.sleep(1.8)
pyautogui.press("enter")
time.sleep(8.5)
pyautogui.click(x=941, y=606)
time.sleep(1)
pyautogui.click(x=918, y=395)
time.sleep(1)
sys.exit(0) 