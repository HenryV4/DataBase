# dao/HotelAmenitiesDAO.py
# dao/HotelAmenitiesDAO.py
from flask import current_app

class HotelAmenitiesDAO:
    @staticmethod
    def get_amenities_by_hotel(hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT a.id, a.name
                FROM amenities a
                JOIN hotel_has_amenities ha ON a.id = ha.amenities_id
                WHERE ha.hotel_id = %s
            """, (hotel_id,))
            amenities = cursor.fetchall()
            cursor.close()
            return [HotelAmenitiesDAO._to_dict(amenity) for amenity in amenities]
        except Exception as e:
            current_app.logger.error(f"Error retrieving amenities for hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error retrieving amenities for hotel {hotel_id}: {str(e)}")

    @staticmethod
    def _to_dict(amenity_row):
        """Convert a hotel amenity row from the database into a dictionary"""
        return {
            "id": amenity_row[0],
            "name": amenity_row[1]
        }


    @staticmethod
    def add_amenity_to_hotel(hotel_id, amenity_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO hotel_has_amenities (hotel_id, amenities_id) VALUES (%s, %s)", (hotel_id, amenity_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error adding amenity to hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error adding amenity to hotel {hotel_id}: {str(e)}")

    @staticmethod
    def remove_amenity_from_hotel(hotel_id, amenity_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM hotel_has_amenities WHERE hotel_id = %s AND amenities_id = %s", (hotel_id, amenity_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error removing amenity from hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error removing amenity from hotel {hotel_id}: {str(e)}")
