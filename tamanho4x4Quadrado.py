import pyautogui
import time
import sys

pyautogui.press("win")
time.sleep(1)
pyautogui.write("google") # Abre o navegador
time.sleep(1)
pyautogui.press("enter")
time.sleep(3.4)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=742, y=65)  # clica Barra de pesquisa
time.sleep(2)
pyautogui.write("doc.new")  
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey('win', 'm')  # Minimiza todas as janelas
time.sleep(1)
pyautogui.doubleClick(x=1850, y=798)# Abre pasta
time.sleep(1)
pyautogui.hotkey('win', 'up')
time.sleep(0.5) 
pyautogui.click(x=232, y=142)  # clica na foto
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')  # Copia
time.sleep(1)
pyautogui.hotkey('alt','tab') # Volta no navegador
time.sleep(1)
pyautogui.click(x=564, y=293) # clica no documento 
pyautogui.hotkey('ctrl', 'v')  # Cola
time.sleep(1)
pyautogui.click(x=582, y=300) # seleciona a imagem
time.sleep(1)
pyautogui.click(x=971, y=201)  # clica em op. de imagem
time.sleep(1)
pyautogui.click(x=1718, y=273) # tamanho e rotação
time.sleep(0.5)
pyautogui.press("tab") # passa para largura
time.sleep(0.5)
pyautogui.write("4") # digita 4
pyautogui.click(x=1694, y=501) # clica em altura
time.sleep(0.5)
pyautogui.click(x=1783, y=368) # clica em uma das fotos
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')   # junta todas
time.sleep(0.5)
pyautogui.write("4")
time.sleep(0.5)
pyautogui.click(x=423, y=302) # seleciona a imagem
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')  
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')  
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'v') 
pyautogui.hotkey('ctrl', 'a') 
pyautogui.click(x=1038, y=211) # espaçamento
time.sleep(1)
pyautogui.click(x=1073, y=343) # espaçamento duplo
time.sleep(1)
pyautogui.click(x=1108, y=353)  # clica em cima do documento
time.sleep(1)
pyautogui.hotkey('ctrl', 'a') # seleciona todos
time.sleep(1)
pyautogui.click(x=997, y=209) # clica em alinhar
time.sleep(0.5)
pyautogui.click(x=1031, y=242) # clica em alinhar centralizado
time.sleep(0.5)
pyautogui.click(x=86, y=162)  # clica em arquivo
time.sleep(0.2)
pyautogui.click(x=155, y=377)  # clica em fazer download
time.sleep(0.2)
pyautogui.click(x=493, y=486) # clica em salvar pdf
time.sleep(0.7)
pyautogui.press("win")
sys.exit(0) 


