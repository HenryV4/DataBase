from flask import Blueprint
from ..controllers.ClientHotelController import ClientHotelController

client_hotel_bp = Blueprint('client_hotel', __name__)

@client_hotel_bp.route('/client-hotel/add', methods=['POST'])
def add_client_hotel_relation():
    return ClientHotelController.add_client_hotel_relation()
