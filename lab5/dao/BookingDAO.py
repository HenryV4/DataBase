from flask import current_app

class BookingDAO:
    @staticmethod
    def get_all_bookings():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT booking_id, check_in_date, check_out_date,
                       total_price, room_id, client_id, payment_id
                FROM booking
            """)
            rows = cursor.fetchall()
            return [BookingDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving bookings: {str(e)}")
            raise Exception(f"Error retrieving bookings: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        booking_id, check_in, check_out, total_price, room_id, client_id, payment_id = row
        return {
            "booking_id": booking_id,  # лише назва таблиці + _id
            "check_in_date": str(check_in) if check_in is not None else None,
            "check_out_date": str(check_out) if check_out is not None else None,
            "total_price": float(total_price) if total_price is not None else None,
            "room_id": room_id,
            "client_id": client_id,
            "payment_id": payment_id
        }

    @staticmethod
    def insert_booking(check_in_date, check_out_date, total_price, room_id, client_id, payment_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO booking
                    (check_in_date, check_out_date, total_price, room_id, client_id, payment_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (check_in_date, check_out_date, total_price, room_id, client_id, payment_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            current_app.logger.error(f"Error inserting booking: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error inserting booking: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_booking(booking_id, check_in_date, check_out_date, total_price, room_id, client_id, payment_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE booking
                SET check_in_date=%s,
                    check_out_date=%s,
                    total_price=%s,
                    room_id=%s,
                    client_id=%s,
                    payment_id=%s
                WHERE booking_id=%s
            """, (check_in_date, check_out_date, total_price, room_id, client_id, payment_id, booking_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error updating booking {booking_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error updating booking {booking_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_booking(booking_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM booking WHERE booking_id=%s", (booking_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error deleting booking {booking_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error deleting booking {booking_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
