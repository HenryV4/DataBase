# routes/BookingRoute.py
from flask import Blueprint
from ..controllers.BookingController import BookingController

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/bookings', methods=['GET'])
def get_bookings():
    return BookingController.get_all_bookings()

@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    return BookingController.create_booking()

@booking_bp.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    return BookingController.update_booking(booking_id)

@booking_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    return BookingController.delete_booking(booking_id)
