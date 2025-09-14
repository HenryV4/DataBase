from flask import Blueprint
from controllers.HotelController import HotelController

hotel_bp = Blueprint('hotel_bp', __name__)

@hotel_bp.route('/hotels', methods=['GET'])
def get_hotels():
    return HotelController.get_all_hotels()

@hotel_bp.route('/hotels/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    return HotelController.get_hotel(hotel_id)

@hotel_bp.route('/hotels', methods=['POST'])
def create_hotel():
    return HotelController.create_hotel()

@hotel_bp.route('/hotels/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    return HotelController.update_hotel(hotel_id)

@hotel_bp.route('/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    return HotelController.delete_hotel(hotel_id)

