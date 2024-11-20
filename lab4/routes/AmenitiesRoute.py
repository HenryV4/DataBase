# routes/AmenitiesRoute.py
from flask import Blueprint
from controllers.AmenitiesController import AmenitiesController

# Creating the Blueprint for Amenities
amenities_bp = Blueprint('amenities_bp', __name__)

# Amenities Routes
@amenities_bp.route('/amenities', methods=['GET'])
def get_amenities():
    return AmenitiesController.get_all_amenities()

@amenities_bp.route('/amenities', methods=['POST'])
def create_amenity():
    return AmenitiesController.create_amenity()

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    return AmenitiesController.update_amenity(amenity_id)

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    return AmenitiesController.delete_amenity(amenity_id)
