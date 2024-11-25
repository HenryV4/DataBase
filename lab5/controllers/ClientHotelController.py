from flask import request, jsonify
from ..dao.ClientHotelDAO import ClientHotelDAO

class ClientHotelController:
    @staticmethod
    def add_client_hotel_relation():
        try:
            data = request.get_json()
            client_name = data['client_name']
            hotel_name = data['hotel_name']

            result = ClientHotelDAO.insert_relation(client_name, hotel_name)
            if result['status'] == "error":
                return jsonify(result), 400  # Помилка для клієнта
            return jsonify(result), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

