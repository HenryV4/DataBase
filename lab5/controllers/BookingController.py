from flask import jsonify, request
from dao.BookingDAO import BookingDAO

class BookingController:
    @staticmethod
    def get_all_bookings():
        try:
            bookings = BookingDAO.get_all_bookings()
            return jsonify(bookings), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_booking():
        try:
            data = request.get_json()
            BookingDAO.insert_booking(data['check_in_date'], data['check_out_date'], data['total_price'], data['room_id'], data['client_id'], data['payment_id'])
            return jsonify({'message': 'Booking created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_booking(booking_id):
        try:
            data = request.get_json()
            BookingDAO.update_booking(booking_id, data['check_in_date'], data['check_out_date'], data['total_price'], data['room_id'], data['client_id'], data['payment_id'])
            return jsonify({'message': 'Booking updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_booking(booking_id):
        try:
            BookingDAO.delete_booking(booking_id)
            return jsonify({'message': 'Booking deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
