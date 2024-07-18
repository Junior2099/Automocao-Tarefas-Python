import pyautogui
import time
import sys

pyautogui.press("win")
time.sleep(1)
pyautogui.write("google") # Abre o navegador
time.sleep(1)
pyautogui.press("enter")
time.sleep(3.3)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=742, y=65)  # clica na barra de endereço
time.sleep(2)
pyautogui.write("doc.new")  #  digita o site para
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey('ctrl', 't') 
time.sleep(1)
pyautogui.write("https://web.whatsapp.com/")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=298, y=222)# clica na pesquisa 
time.sleep(2)
pyautogui.write("José")
time.sleep(2)
pyautogui.click(x=401, y=319)# clica no meu perfil 
time.sleep(4)
pyautogui.click(x=1569, y=739)# clica na foto para baixar
time.sleep(1)
pyautogui.click(x=1831, y=148)# clica para baixar a foto
time.sleep(1)
pyautogui.hotkey('win', 'm')  # Minimiza todas as janelas
time.sleep(1)
pyautogui.doubleClick(x=1850, y=798)# Abre pasta
time.sleep(1)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=232, y=154)# clica na foto
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.hotkey('alt','tab') 
time.sleep(1)
pyautogui.hotkey('ctrl','tab')  #altera para a janela do Google Docs
time.sleep(1)
pyautogui.click(x=1217, y=291) #clica no documento
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.click(x=583, y=300) # clica na foto novamente
time.sleep(1)
pyautogui.click(x=1016, y=204) # clica em opções de imagem
time.sleep(1)
pyautogui.click(x=1718, y=279) #tamanho e rotação
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.write("3")
pyautogui.click(x=1657, y=506) # desbloqueia proporção
time.sleep(1)
pyautogui.click(x=1787, y=376) # seleciona altura
time.sleep(1.8)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1.8)
pyautogui.write("4")
time.sleep(1.8)
pyautogui.click(x=842, y=615) # seleciona altura
pyautogui.press('up', presses=7)
time.sleep(1)
pyautogui.click(x=86, y=162)  # clica em arquivo
time.sleep(0.9)
pyautogui.click(x=155, y=377)  # clica em fazer download
time.sleep(0.8)
pyautogui.click(x=493, y=486) # clica em salvar pdf
time.sleep(1)
pyautogui.press("win")
sys.exit(0) 