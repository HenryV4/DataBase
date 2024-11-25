# controllers/ClientController.py
from flask import jsonify, request
from ..dao.ClientDAO import ClientDAO

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
        
    @staticmethod
    def add_client():
        """Calls the insert_client stored procedure to add a new client"""
        try:
            data = request.get_json()
            full_name = data['full_name']
            email = data['email']
            phone_num = data['phone_num']
            discount_cards_id = data.get('discount_cards_id')
            loyalty_program_id = data.get('loyalty_program_id')  # Додаємо поле

            result = ClientDAO.insert_client(full_name, email, phone_num, discount_cards_id, loyalty_program_id)
            return jsonify(result), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    # @staticmethod
    # def get_stat():
    #     try:
    #         data = request.get_json()
    #         table_name = data.get('table')
    #         column_name = data.get('column')
    #         operation = data.get('operation')

    #         if not table_name:
    #             return jsonify({"error": "Table name is required"}), 400
    #         if not column_name:
    #             return jsonify({"error": "Column name is required"}), 400
    #         if operation not in ['MAX', 'MIN', 'SUM', 'AVG']:
    #             return jsonify({"error": "Invalid operation. Allowed: MAX, MIN, SUM, AVG"}), 400

    #         result = ClientDAO.calculate_stat(table_name, column_name, operation)
    #         return jsonify(result), 200
    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500
