# controllers/HotelController.py
from flask import jsonify, request
from dao.HotelDAO import HotelDAO

class HotelController:
    @staticmethod
    def get_all_hotels():
        try:
            hotels = HotelDAO.get_all_hotels()
            return jsonify(hotels), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_hotel():
        try:
            data = request.get_json()
            HotelDAO.insert_hotel(
                data['name'], data['address'], data['room_num'], data['location_id'], data['stars'], data['chain_id']
            )
            return jsonify({'message': 'Hotel created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_hotel(hotel_id):
        try:
            data = request.get_json()
            HotelDAO.update_hotel(
                hotel_id, data['name'], data['address'], data['room_num'], data['location_id'], data['stars'], data['chain_id']
            )
            return jsonify({'message': 'Hotel updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_hotel(hotel_id):
        try:
            HotelDAO.delete_hotel(hotel_id)
            return jsonify({'message': 'Hotel deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

