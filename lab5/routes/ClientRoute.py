from flask import Blueprint
from controllers.ClientController import ClientController

client_bp = Blueprint('client_bp', __name__)

# Existing routes
@client_bp.route('/clients', methods=['GET'])
def get_clients():
    return ClientController.get_all_clients()

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    return ClientController.get_client(client_id)

@client_bp.route('/clients', methods=['POST'])
def create_client():
    return ClientController.create_client()

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    return ClientController.update_client(client_id)

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    return ClientController.delete_client(client_id)

@client_bp.route('/clients/<city>', methods=['GET'])
def get_clients_by_city(city):
    return ClientController.get_clients_by_city(city)

@client_bp.route('/client/add', methods=['POST'])
def add_client():
    return ClientController.add_client()

