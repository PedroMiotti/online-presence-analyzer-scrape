import Company
from companies import Correios, PicPay, Ifood
from Factory import Factory


class CompanyFactory(Factory):

    def companyToScrape(self, company_name) -> Company:
        if company_name == "picpay":
            return PicPay()
        elif company_name == "ifood":
            return Ifood()
        elif company_name == "correios":
            return Correios()
