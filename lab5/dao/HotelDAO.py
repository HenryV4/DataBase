from flask import current_app

class HotelDAO:
    @staticmethod
    def get_all_hotels():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT hotel_id, name, address, room_num, location_id, stars, chain_id
                FROM hotel
            """)
            rows = cursor.fetchall()
            return [HotelDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving hotels: {str(e)}")
            raise Exception(f"Error retrieving hotels: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """
        row = (hotel_id, name, address, room_num, location_id, stars, chain_id)
        """
        hotel_id, name, address, room_num, location_id, stars, chain_id = row
        return {
            "hotel_id": hotel_id,                     # лише <table>_id у JSON
            "name": name,
            "address": address,
            "room_num": int(room_num) if room_num is not None else None,
            "location_id": location_id,
            "stars": float(stars) if stars is not None else None,
            "chain_id": chain_id
        }

    @staticmethod
    def insert_hotel(name, address, room_num, location_id, stars, chain_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO hotel (name, address, room_num, location_id, stars, chain_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, address, room_num, location_id, stars, chain_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # новий hotel_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting hotel: {str(e)}")
            raise Exception(f"Error inserting hotel: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_hotel(hotel_id, name, address, room_num, location_id, stars, chain_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE hotel
                SET name=%s,
                    address=%s,
                    room_num=%s,
                    location_id=%s,
                    stars=%s,
                    chain_id=%s
                WHERE hotel_id=%s
            """, (name, address, room_num, location_id, stars, chain_id, hotel_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error updating hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_hotel(hotel_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM hotel WHERE hotel_id=%s", (hotel_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error deleting hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
