from Company import Company
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils.extrair_inteiro import extrair_inteiro


class PicPay(Company):

    def execute(self) -> str:
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get('https://www.reclameaqui.com.br/')

        input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )

        input.send_keys('PicPay')
        input.send_keys(Keys.RETURN)

        link_pagina = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="PicPay"]'))
        )
        link_pagina.click()

        driver.execute_script("window.scrollTo(0, 300)")

        select_geral = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Geral']"))
        )
        select_geral.click()

        dados = {}

        rep_geral = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[1]/div[2]/span[2]/b')

        reclamacoes = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[2]/a[1]/div/div/b')

        respondidas = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[2]/a[2]/div/div/b')

        pct_resp = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[1]/span')

        pct_volt = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[2]/span')

        ind_sol = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[3]/span')

        nota = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[4]/span')

        n_resp = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[2]/div[1]/a/div/b')

        avaliadas = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[2]/div[2]/a/div/b')


        dados['Reputacao_geral'] = rep_geral.text
        dados['Reclamacoes_total'] = reclamacoes.text
        dados['Respondidas_total'] = respondidas.text
        dados['Porcentagem_resp'] = pct_resp.text
        dados['Voltaria_negocio'] = pct_volt.text
        dados['Indice_solucao'] = ind_sol.text
        dados['Nota'] = nota.text
        dados['N_respondidas'] = n_resp.text
        dados['Avaliadas'] = avaliadas.text

        # driver.close()

        return dados
