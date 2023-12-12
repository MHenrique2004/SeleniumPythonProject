from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver_service = Service(executable_path='C:\Windows\chromedriver.exe')
browser = webdriver.Chrome(service = driver_service)
import pandas as pd

tabela = pd.read_excel('Emitir.xlsx')

for i, cpf in enumerate(tabela["CPF"]):
    nome = tabela.loc[i, "Nome"]
    email = tabela.loc[i,"Email"]
    descricao = tabela.loc[i,"Descrição"]
    valor = tabela.loc[i,"Valor"]
    browser.get('https://forms.gle/h6k8SGXDTCohdmeM9')

    cppf = browser.find_element("xpath",
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cpf)

    Noome = browser.find_element("xpath",
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nome)

    emaill = browser.find_element("xpath",
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(email)
    desc = browser.find_element("xpath",
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(descricao)

    val = browser.find_element("xpath",
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(valor))

    browser.find_element("xpath",
                         '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()