from Company import Company
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Correios(Company):

    def execute(self, driver) -> str:
        dados = {}
        dados["empresa_id"] = 3
        dados["nome_empresa"] = "Correios"

        waittime=10

        driver.get('https://www.reclameaqui.com.br/empresa/correios/')

        driver.execute_script("window.scrollTo(0, 300)")

        select_geral = WebDriverWait(driver, waittime).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Geral']"))
        )

        time.sleep(2)

        select_geral.click()

        rep_geral = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[1]/div[2]/span[2]/b')

        reclamacoes = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[2]/a[1]/div/div/b')

        respondidas = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[1]/div[2]/a[2]/div/div/b')

        pct_resp = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[1]/span')

        pct_volt = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[2]/span')

        ind_sol = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[3]/span')

        nota = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[1]/div[4]/span')

        n_resp = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[2]/div[1]/a/div/b')

        avaliadas = driver.find_element(By.XPATH, '//*[@id="reputation"]/div[2]/div[2]/div[2]/a/div/b')

        dados['reputacao_geral'] = rep_geral.text
        dados['reclamacoes_total'] = reclamacoes.text
        dados['respondidas_total'] = respondidas.text
        dados['porcentagem_resp'] = pct_resp.text
        dados['voltaria_negocio'] = pct_volt.text
        dados['indice_solucao'] = ind_sol.text
        dados['nota'] = nota.text
        dados['n_respondidas'] = n_resp.text
        dados['avaliadas'] = avaliadas.text

        return dados
