from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def companyToScrape(self):
        pass

    def scrape(self):
        company = self.companyToScrape()

        result = company.execute()

        return result
