
# passo a passo do projeto 

#passo 1 - Entrar no sistema da empresa 
  # LINK 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

import pyautogui 
import time
import pandas as pd 

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
#pyautogui.PAUSE = 1 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1)

#Passo 2 - Fazer login

pyautogui.click(x=1088, y=352)
pyautogui.write('thiago.assis@gmail.com')
pyautogui.press('tab')
pyautogui.write('161922')
pyautogui.press('tab')
pyautogui.press('enter')

#Passo 3 - Importar uma base de dados

tabela = pd.read_csv('produtos.csv')
#print(tabela)

#Passo 4 - Cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=1419, y=124)
    time.sleep(1)
    pyautogui.click(x=1018, y=259)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)

 
#Passo 5 - Repetir isso ate acabar a base atraves do FOR feito na linha 37