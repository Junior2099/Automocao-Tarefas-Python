import pyautogui
import time
import sys

pyautogui.press("win")
time.sleep(1)
pyautogui.write("google") # Abre o navegador
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=871, y=60)  # clica na barra de endereço
time.sleep(1)
pyautogui.write("https://web.whatsapp.com/")  #  digita o site para
time.sleep(1)
pyautogui.press("enter")
time.sleep(8)
pyautogui.click(x=289, y=219)# clica na pesquisa 
time.sleep(3)
pyautogui.write("José")
time.sleep(2)
pyautogui.click(x=401, y=319)# clica no meu perfil 
time.sleep(9)
pyautogui.click(x=1569, y=739)# clica na foto para baixar
time.sleep(3)
pyautogui.click(x=1831, y=148)# clica para baixar a foto
time.sleep(2)
pyautogui.hotkey('win', 'm')  # Minimiza todas as janelas
time.sleep(1)
pyautogui.doubleClick(x=1850, y=798)# Abre pasta Downloads
time.sleep(1)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=232, y=154)# clica na foto
time.sleep(1)
pyautogui.rightClick()
time.sleep(1)
pyautogui.click(x=339, y=596) # Abrir com
time.sleep(1)
pyautogui.click(x=631, y=741) # paint
time.sleep(1)
pyautogui.hotkey('win', 'up') # maximiza a tela
time.sleep(1)
pyautogui.click(x=99, y=129) # remove o fundo
time.sleep(5)
pyautogui.click(x=191, y=109) # alongar e distorcer
time.sleep(1)
pyautogui.click(x=975, y=427) # seleciona pixels
time.sleep(1)
pyautogui.click(x=953, y=503) # desbloqueia
time.sleep(1)
pyautogui.click(x=880, y=503)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a') 
time.sleep(1)
pyautogui.write("354")
time.sleep(1)
pyautogui.click(x=1025, y=502)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a') 
time.sleep(1)
pyautogui.write("472")
time.sleep(1)
pyautogui.click(x=894, y=688)
time.sleep(1)
pyautogui.hotkey('alt', 'F4') 
time.sleep(1)
pyautogui.press("enter")


pyautogui.hotkey('win', 'm')  # Minimiza todas as janelas
time.sleep(7)
pyautogui.doubleClick(x=1630, y=655)# abre arquivo FOTO 3x4.PSD
time.sleep(13)
pyautogui.hotkey('win', 'up') 
time.sleep(6)
pyautogui.click(x=1817, y=670)# clica na segunda layer do projeto
time.sleep(1)
pyautogui.hotkey('alt', 'tab') 
time.sleep(1)
pyautogui.moveTo(232, 154) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=823, y=513, duration=3) 
time.sleep(1)
pyautogui.hotkey('alt', 'tab') 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto
time.sleep(1)
pyautogui.click(x=1827, y=1026)# duplica a foto
time.sleep(1)
pyautogui.click(x=1827, y=1026)# duplica a foto
time.sleep(1)
pyautogui.click(x=1827, y=1026)# duplica a foto
time.sleep(1)
pyautogui.click(x=1827, y=1026)# duplica a foto
time.sleep(1)
pyautogui.click(x=1827, y=1026)# duplica a foto
time.sleep(1)

# 1 foto
pyautogui.moveTo(935, 491) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=674, y=345, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto


# 2 foto
pyautogui.moveTo(935, 491) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=930, y=340, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto

# 3 foto 
pyautogui.moveTo(944, 624) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=1190, y=459, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto

# 4 foto
pyautogui.moveTo(944, 624) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=693, y=783, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto

# 5 foto   
pyautogui.moveTo(930, 633) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=930, y=801, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto
time.sleep(2)

pyautogui.click(x=1732, y=783)# esconde foto
time.sleep(2)

# 6 foto
pyautogui.moveTo(930, 633) # pega a foto
time.sleep(1)
pyautogui.mouseDown() # clica
time.sleep(1)
pyautogui.moveTo(x=1174, y=800, duration=3) 
time.sleep(1)
pyautogui.mouseUp() # solta no projeto
time.sleep(1)
pyautogui.click(x=1732, y=783)# mostra foto
time.sleep(1)
pyautogui.click(x=23, y=36)# clica em arquivo
time.sleep(1)
pyautogui.click(x=74, y=373)# clica em exporta como
time.sleep(1)
pyautogui.click(x=71, y=278)# clica em desktop
time.sleep(1)
pyautogui.click(x=594, y=107)# clica na barra de pesquisa
time.sleep(1)
pyautogui.click(x=594, y=107)# clica na pesquisa
time.sleep(1)
for _ in range(3):
    pyautogui.press('backspace')
time.sleep(1)
pyautogui.write("png")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2.5)
pyautogui.click(x=1047, y=771)# clica para exportar
time.sleep(1)
pyautogui.hotkey('alt', 'F4') 
time.sleep(2.5)
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('win', 'm') 
sys.exit(0) 
