from flask import Blueprint
from controllers.BookingLogController import BookingLogController

booking_log_bp = Blueprint('booking_log', __name__)

@booking_log_bp.route('/logs', methods=['GET'])
def get_logs():
    return BookingLogController.get_logs()
