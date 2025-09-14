from flask import Blueprint
from controllers.HotelAmenitiesController import HotelAmenitiesController

hotel_amenities_bp = Blueprint('hotel_amenities_bp', __name__)

@hotel_amenities_bp.route('/hotels/<int:hotel_id>/amenities', methods=['GET'])
def get_amenities_for_hotel(hotel_id):
    return HotelAmenitiesController.get_amenities_for_hotel(hotel_id)

@hotel_amenities_bp.route('/hotels/<int:hotel_id>/amenities', methods=['POST'])
def add_amenity_to_hotel(hotel_id):
    return HotelAmenitiesController.add_amenity_to_hotel(hotel_id)

@hotel_amenities_bp.route('/hotels/<int:hotel_id>/amenities/<int:amenity_id>', methods=['DELETE'])
def remove_amenity_from_hotel(hotel_id, amenity_id):
    return HotelAmenitiesController.remove_amenity_from_hotel(hotel_id, amenity_id)
