from flask import jsonify
from dao.BookingLogDAO import BookingLogDAO

class BookingLogController:
    @staticmethod
    def get_logs():
        try:
            result = BookingLogDAO.get_logs()
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
