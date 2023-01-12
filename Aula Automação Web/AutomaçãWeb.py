import pyautogui
import pandas as pd
import plotly.express as px

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()


#Pegando a cotação do Euro
navegador.get('https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)


#Pegando a cotação do Dólar
navegador.get('https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)


# Pegando a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)


#Usando Pandas para importar a base de dados
tabela = pd.read_excel('Produtos.xlsx')


#Atualizando a cotação das moedas
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

#Atualizando o preço de compra
tabela['Preço de Compra'] = tabela['Cotação'] * tabela['Preço Original']


#Atualizando o preço de venda
tabela['Preço de Venda'] = tabela['Margem'] * tabela['Preço de Compra']


#Exportar base de dados
tabela.to_excel("Produto Novo.xlsx", index = False)

