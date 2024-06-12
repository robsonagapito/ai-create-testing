# app.py
from flask import Flask
from flask_restx import Api
from routes.routes import api as customers

app = Flask(__name__)
api = Api(app, title='Cadastro de Clientes API', version='1.0', description='API simples para cadastro de clientes')

api.add_namespace(customers)

if __name__ == '__main__':
    app.run(debug=True)
