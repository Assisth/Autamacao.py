import pyautogui 
import time
import pandas as pd

time.sleep(5)
print(pyautogui.position()) #achar posição no pc Ex. mouse

tabela = pd.read_csv('produtos.csv')
print(tabela)