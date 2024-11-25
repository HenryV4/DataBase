from flask import current_app

class BookingLogDAO:
    @staticmethod
    def get_logs():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM booking_log")
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            raise Exception(f"Error fetching logs: {str(e)}")
