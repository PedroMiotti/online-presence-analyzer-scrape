from flask import Flask, request
from utils.response import response

app = Flask(__name__)


@app.route('/run', methods=["GET"])
def run_all():
    return response(200, "Run all services")


@app.route('/run/<company_name>', methods=["GET"])
def run_one(company_name):
    return response(200, f'Run only one company : {company_name}')


if __name__ == '__main__':
    app.run()
