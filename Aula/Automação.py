import pyautogui
import pyperclip
import time
import pandas as pd
import numpy




pyautogui.PAUSE = 1

#Abrindo aba win
pyautogui.press('win')
time.sleep(2)
#pesquisando pelo google chrome
pyautogui.write('Chrome')     
time.sleep(2)      
# abrindo chrome
pyautogui.press('enter')
time.sleep(2)
# Selecionando usuario
pyautogui.click(x=737, y=430)
time.sleep(2)
# abrindo uma nova guia
pyautogui.hotkey('ctrl', 't')
time.sleep(2)
# pesquisando Gmail
pyautogui.write('gmail.com')
time.sleep(2)
# Abrindo Gmail
pyautogui.press('enter')


