# controllers/LocationController.py
from flask import jsonify, request
from dao.LocationDAO import LocationDAO

class LocationController:
    @staticmethod
    def get_all_locations():
        try:
            locations = LocationDAO.get_all_locations()
            return jsonify(locations), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_location(location_id):
        try:
            location = LocationDAO.get_location_by_id(location_id)
            if location:
                return jsonify(location), 200
            return jsonify({"message": "Location not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_location():
        try:
            data = request.get_json()
            LocationDAO.insert_location(data['city'], data['country'])
            return jsonify({'message': 'Location created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_location(location_id):
        try:
            data = request.get_json()
            LocationDAO.update_location(location_id, data['city'], data['country'])
            return jsonify({'message': 'Location updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_location(location_id):
        try:
            LocationDAO.delete_location(location_id)
            return jsonify({'message': 'Location deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
