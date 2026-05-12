# controllers/AmenitiesController.py
from flask import jsonify, request
from dao.AmenitiesDAO import AmenitiesDAO

class AmenitiesController:
    @staticmethod
    def get_all_amenities():
        try:
            amenities = AmenitiesDAO.get_all_amenities()
            return jsonify(amenities), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_amenity():
        try:
            data = request.get_json()
            AmenitiesDAO.insert_amenity(data['name'])
            return jsonify({'message': 'Amenity created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_amenity(amenity_id):
        try:
            data = request.get_json()
            AmenitiesDAO.update_amenity(amenity_id, data['name'])
            return jsonify({'message': 'Amenity updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_amenity(amenity_id):
        try:
            AmenitiesDAO.delete_amenity(amenity_id)
            return jsonify({'message': 'Amenity deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
