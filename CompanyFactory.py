import Company
from companies.Correios import Correios
from companies.Ifood import Ifood
from companies.PicPay import PicPay
from Factory import Factory


class CompanyFactory(Factory):

    def companyToScrape(self, company_name) -> Company:
        if company_name == "picpay":
            return PicPay()
        elif company_name == "ifood":
            return Ifood()
        elif company_name == "correios":
            return Correios()
