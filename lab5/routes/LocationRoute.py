from flask import Blueprint
from controllers.LocationController import LocationController

location_bp = Blueprint('location_bp', __name__)

@location_bp.route('/locations', methods=['GET'])
def get_locations():
    return LocationController.get_all_locations()

@location_bp.route('/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
    return LocationController.get_location(location_id)

@location_bp.route('/locations', methods=['POST'])
def create_location():
    return LocationController.create_location()

@location_bp.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    return LocationController.update_location(location_id)

@location_bp.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    return LocationController.delete_location(location_id)
