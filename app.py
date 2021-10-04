from flask import Flask, request
from CompanyFactory import CompanyFactory
from utils.response import response

app = Flask(__name__)


@app.route('/run', methods=["GET"])
def run_all():
    return response(200, "Run all services")


@app.route('/run/<company_name>', methods=["GET"])
def run_one(company_name):
    factory = CompanyFactory()
    dados = factory.scrape(company_name)
    return response(200, "Successo", f'Empresa: {company_name}', dados)


if __name__ == '__main__':
    app.run()
