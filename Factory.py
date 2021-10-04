from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):


    @abstractmethod
    def companyToScrape(self):
        pass

    def scrape(self, company_name):
        company = self.companyToScrape(company_name)

        result = company.execute()

        return result

