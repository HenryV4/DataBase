# controllers/ClientController.py
from flask import jsonify, request
from dao.ClientDAO import ClientDAO

class ClientController:
    @staticmethod
    def get_all_clients():
        try:
            clients = ClientDAO.get_all_clients()
            return jsonify(clients), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_client():
        try:
            data = request.get_json()
            ClientDAO.insert_client(data['full_name'], data['email'], data['phone_num'], data.get('discount_cards_id'))
            return jsonify({'message': 'Client created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_client(client_id):
        try:
            data = request.get_json()
            ClientDAO.update_client(client_id, data['full_name'], data['email'], data['phone_num'], data.get('discount_cards_id'))
            return jsonify({'message': 'Client updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_client(client_id):
        try:
            ClientDAO.delete_client(client_id)
            return jsonify({'message': 'Client deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_clients_by_city(city):
        try:
            clients = ClientDAO.get_clients_by_city(city)
            return jsonify(clients), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
