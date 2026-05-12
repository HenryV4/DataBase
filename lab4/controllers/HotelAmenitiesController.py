# controllers/HotelAmenitiesController.py
from flask import jsonify, request
from dao.HotelAmenitiesDAO import HotelAmenitiesDAO

class HotelAmenitiesController:
    @staticmethod
    def get_amenities_for_hotel(hotel_id):
        try:
            amenities = HotelAmenitiesDAO.get_amenities_for_hotel(hotel_id)
            return jsonify(amenities), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def add_amenity_to_hotel(hotel_id):
        try:
            data = request.get_json()
            HotelAmenitiesDAO.add_amenity_to_hotel(hotel_id, data['amenity_id'])
            return jsonify({'message': 'Amenity added to hotel successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def remove_amenity_from_hotel(hotel_id, amenity_id):
        try:
            HotelAmenitiesDAO.remove_amenity_from_hotel(hotel_id, amenity_id)
            return jsonify({'message': 'Amenity removed from hotel successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
