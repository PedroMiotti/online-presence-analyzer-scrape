from flask import Flask, request
from CompanyFactory import CompanyFactory
from utils.response import response

app = Flask(__name__)


@app.route('/run', methods=["GET"])
def run_all():
    allCompanies = ["picpay", "correios"]
    data = []

    factory = CompanyFactory()
    for company in allCompanies:
        data.append(factory.scrape(company))

    return response(200, "Sucesso", "companies", data)


@app.route('/run/<company_name>', methods=["GET"])
def run_one(company_name):
    factory = CompanyFactory()
    data = factory.scrape(company_name)
    return response(200, "Sucesso", "companies", data)


if __name__ == '__main__':
    app.run()
