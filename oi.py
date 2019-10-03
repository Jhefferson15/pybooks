from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
#url = input('Qual o link da autenticação?')
url = 'https://jigsaw.vitalsource.com/auth/redirects/UFB7DYRJEMUR8E7AP8Z7GBCW5H77B4K7PC53KTSFNWE2MH3JQY'
firefox.get(url)
link_livro = 'https://integrada.minhabiblioteca.com.br/#/books/9788582712306'
firefox.get(link_livro)

sleep(10)
try:
    teste = firefox.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/iframe')
    print(teste)
except:
    print('Erro!')
try:
    teste = firefox.find_element(By.XPATH, '//*[@id="easyXDM_default1422_provider"]')
    print(teste)
except:
    print('Erro!')

firefox.quit()




