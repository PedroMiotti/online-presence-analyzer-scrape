import Company
from companies.Correios import Correios
from companies.Ifood import Ifood
from companies.PicPay import PicPay
from companies.NuBank import NuBank
from companies.MagazineLuiza import MagazineLuiza
from companies.MercadoLivre import MercadoLivre
from Factory import Factory


class CompanyFactory(Factory):

    def companyToScrape(self, company_name) -> Company:
        if company_name == "picpay":
            return PicPay()
        elif company_name == "ifood":
            return Ifood()
        elif company_name == "correios":
            return Correios()
        elif company_name == "mercado-livre":
            return MercadoLivre()
        elif company_name == "nubank":
            return NuBank()
        elif company_name == "magalu":
            return MagazineLuiza()
