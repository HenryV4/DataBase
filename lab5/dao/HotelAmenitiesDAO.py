from flask import current_app

class HotelAmenitiesDAO:
    @staticmethod
    def get_amenities_for_hotel(hotel_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT a.amenities_id, a.name
                FROM amenities a
                JOIN hotel_has_amenities ha ON a.amenities_id = ha.amenities_id
                WHERE ha.hotel_id = %s
            """, (hotel_id,))
            rows = cursor.fetchall()
            return [HotelAmenitiesDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving amenities for hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error retrieving amenities for hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """row = (amenities_id, name)"""
        return {
            "amenities_id": row[0],  # лише <table>_id у JSON
            "name": row[1]
        }

    @staticmethod
    def add_amenity_to_hotel(hotel_id: int, amenities_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO hotel_has_amenities (hotel_id, amenities_id) VALUES (%s, %s)",
                (hotel_id, amenities_id)
            )
            current_app.mysql.connection.commit()
            return {"status": "success"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error adding amenity {amenities_id} to hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error adding amenity to hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def remove_amenity_from_hotel(hotel_id: int, amenities_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "DELETE FROM hotel_has_amenities WHERE hotel_id=%s AND amenities_id=%s",
                (hotel_id, amenities_id)
            )
            current_app.mysql.connection.commit()
            return {"status": "success"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error removing amenity {amenities_id} from hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error removing amenity from hotel {hotel_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
