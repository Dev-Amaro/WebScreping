from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando nosso robô...")

arq = open("resultado.txt", "w")
workbook = xlrd.open_workbook('C:\\Users\\Jefferson Herbert\\Desktop\\dominios.xls')
sheet = workbook.sheet_by_name('Planilha1')
rows = sheet.nrows
coluns = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

driver = webdriver.Chrome('C:\\Users\\Jefferson Herbert\\Desktop\\chromedriver.exe', options=options)
driver.get("https://registro.br/")

for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element_by_id("is-avail-field")
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(keys.Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    texto = "Dominio %s %s\n" % (x, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    arq.write(texto)

arq.close()
driver.close()