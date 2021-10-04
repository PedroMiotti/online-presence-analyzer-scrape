from flask import Flask, request
from CompanyFactory import FactoryPicPay
from utils.response import response

app = Flask(__name__)


@app.route('/run', methods=["GET"])
def run_all():
    return response(200, "Run all services")


@app.route('/run/<company_name>', methods=["GET"])
def run_one(company_name):
    fact = FactoryPicPay()
    dados = fact.scrape()
    return response(200, "Successo" , "PicPay", dados)


if __name__ == '__main__':
    app.run()
