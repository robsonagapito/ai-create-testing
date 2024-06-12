# routes.py
from flask_restx import Namespace, Resource, fields
from models.customer import Customer

api = Namespace('customers', description='Operações relacionadas aos clientes')

customer_model = api.model('Customer', {
    'id': fields.String(readOnly=True, description='O identificador único do cliente'),
    'name': fields.String(required=True, description='O nome do cliente'),
    'age': fields.Integer(required=True, description='A idade do cliente'),
    'nickname': fields.String(required=True, description='O apelido do cliente'),
    'cellphone': fields.String(required=True, description='O telefone do cliente')
})

customers = {}

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_customers')
    @api.marshal_list_with(customer_model)
    def get(self):
        '''Lista todos os clientes'''
        return [customer.to_dict() for customer in customers.values()]

    @api.doc('create_customer')
    @api.expect(customer_model)
    @api.marshal_with(customer_model, code=201)
    def post(self):
        '''Cria um novo cliente'''
        data = api.payload
        customer = Customer(data['name'], data['age'], data['nickname'], data['cellphone'])
        customers[customer.id] = customer
        return customer.to_dict(), 201

@api.route('/<id>')
@api.response(404, 'Cliente não encontrado')
@api.param('id', 'O identificador do cliente')
class CustomerResource(Resource):
    @api.doc('get_customer')
    @api.marshal_with(customer_model)
    def get(self, id):
        '''Obter um cliente pelo ID'''
        customer = customers.get(id)
        if customer is None:
            api.abort(404, "Cliente não encontrado")
        return customer.to_dict()
