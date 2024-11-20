# dao/BookingDAO.py
from flask import current_app

class BookingDAO:
    @staticmethod
    def get_all_bookings():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM booking")
            bookings = cursor.fetchall()
            cursor.close()
            return [BookingDAO._to_dict(booking) for booking in bookings]
        except Exception as e:
            current_app.logger.error(f"Error retrieving bookings: {str(e)}")
            raise Exception(f"Error retrieving bookings: {str(e)}")

    @staticmethod
    def _to_dict(booking_row):
        """Convert a booking row from the database into a dictionary"""
        return {
            "id": booking_row[0],
            "check_in_date": str(booking_row[1]),
            "check_out_date": str(booking_row[2]),
            "total_price": str(booking_row[3]),
            "room_id": booking_row[4],
            "client_id": booking_row[5],
            "payment_id": booking_row[6]
        }


    @staticmethod
    def insert_booking(check_in_date, check_out_date, total_price, room_id, client_id, payment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO booking (check_in_date, check_out_date, total_price, room_id, client_id, payment_id) VALUES (%s, %s, %s, %s, %s, %s)",
                           (check_in_date, check_out_date, total_price, room_id, client_id, payment_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting booking: {str(e)}")
            raise Exception(f"Error inserting booking: {str(e)}")

    @staticmethod
    def update_booking(booking_id, check_in_date, check_out_date, total_price, room_id, client_id, payment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE booking SET check_in_date=%s, check_out_date=%s, total_price=%s, room_id=%s, client_id=%s, payment_id=%s WHERE id=%s",
                           (check_in_date, check_out_date, total_price, room_id, client_id, payment_id, booking_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating booking with ID {booking_id}: {str(e)}")
            raise Exception(f"Error updating booking with ID {booking_id}: {str(e)}")

    @staticmethod
    def delete_booking(booking_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM booking WHERE id=%s", (booking_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting booking with ID {booking_id}: {str(e)}")
            raise Exception(f"Error deleting booking with ID {booking_id}: {str(e)}")
