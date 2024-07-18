import pyautogui
import time
import sys

pyautogui.hotkey('win','m')
time.sleep(1)
pyautogui.doubleClick(x=1850, y=798)# Abre pasta
time.sleep(1)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.doubleClick(x=254, y=166) # clica e abre o PDF
time.sleep(2)
pyautogui.hotkey('ctrl', 'p') # abre opções de imprimir
time.sleep(2)
pyautogui.click(x=687, y=282) # clica nas impressoras
time.sleep(1)
sys.exit(0) # finaliza o programa
