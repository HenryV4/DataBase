from flask import current_app

class RoomDAO:
    @staticmethod
    def get_all_rooms():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT room_id, room_type, price_per_night, available, hotel_id
                FROM room
            """)
            rows = cursor.fetchall()
            return [RoomDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving rooms: {str(e)}")
            raise Exception(f"Error retrieving rooms: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def get_room_by_id(room_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT room_id, room_type, price_per_night, available, hotel_id
                FROM room
                WHERE room_id=%s
            """, (room_id,))
            row = cursor.fetchone()
            return RoomDAO._to_dict(row) if row else None
        except Exception as e:
            current_app.logger.error(f"Error retrieving room {room_id}: {str(e)}")
            raise Exception(f"Error retrieving room {room_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def get_all_rooms_for_hotel(hotel_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT room_id, room_type, price_per_night, available, hotel_id
                FROM room
                WHERE hotel_id=%s
            """, (hotel_id,))
            rows = cursor.fetchall()
            return [RoomDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving rooms for hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error retrieving rooms for hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def insert_room(room_type, price_per_night, available, hotel_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO room (room_type, price_per_night, available, hotel_id)
                VALUES (%s, %s, %s, %s)
            """, (room_type, price_per_night, available, hotel_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # новий room_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting room: {str(e)}")
            raise Exception(f"Error inserting room: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_room(room_id, room_type, price_per_night, available, hotel_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE room
                SET room_type=%s,
                    price_per_night=%s,
                    available=%s,
                    hotel_id=%s
                WHERE room_id=%s
            """, (room_type, price_per_night, available, hotel_id, room_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating room {room_id}: {str(e)}")
            raise Exception(f"Error updating room {room_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_room(room_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM room WHERE room_id=%s", (room_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting room {room_id}: {str(e)}")
            raise Exception(f"Error deleting room {room_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """row = (room_id, room_type, price_per_night, available, hotel_id)"""
        room_id, room_type, price_per_night, available, hotel_id = row
        return {
            "room_id": room_id,
            "room_type": room_type,
            "price_per_night": float(price_per_night) if price_per_night is not None else None,
            "available": bool(available) if available is not None else None,
            "hotel_id": hotel_id
        }
