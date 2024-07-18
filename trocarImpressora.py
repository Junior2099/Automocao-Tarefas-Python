import pyautogui
import time
import sys

pyautogui.hotkey('win','m')
time.sleep(1)
pyautogui.doubleClick(x=1850, y=798)# Abre pasta
time.sleep(1)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.moveTo(254,166) # move o cursor até a foto
pyautogui.click(button='right')# clica com direito na foto
time.sleep(1)
pyautogui.click(x=274, y=244) # clica em imprimir
time.sleep(1)
pyautogui.click(x=677, y=400) # clica nas impressoras para escolher
time.sleep(1)
sys.exit(0) # finaliza o programa
