from __future__ import annotations
from abc import ABC, abstractmethod

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Factory(ABC):

    @abstractmethod
    def companyToScrape(self):
        pass

    def scrape(self, company_name):
        company = self.companyToScrape(company_name)

        self.startDriver()
        result = company.execute(self.driver)
        self.closeDriver()

        return result

    def startDriver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def closeDriver(self):
        self.driver.close()
