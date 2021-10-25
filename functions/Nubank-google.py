from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nomes = [
	'Nubank'
]

driver = webdriver.Chrome()

dados = []

def obterNota(nome_empresa):
	driver.get('https://www.google.com.br/search?q=' + nome_empresa)

	span_nota = WebDriverWait(driver, 20).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.Aq14fc'))
	)

	nota = float(span_nota.text.replace(',', '.'))

	dados.append({
		'nome': nome_empresa,
		'nota': nota
	})

for nome_empresa in nomes:
	obterNota(nome_empresa)

print(dados)

driver.close()
