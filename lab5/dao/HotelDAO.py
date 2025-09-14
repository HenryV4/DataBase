from flask import current_app

class HotelDAO:
    @staticmethod
    def get_all_hotels():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM hotel")
            hotels = cursor.fetchall()
            cursor.close()
            return [HotelDAO._to_dict(hotel) for hotel in hotels]
        except Exception as e:
            current_app.logger.error(f"Error retrieving hotels: {str(e)}")
            raise Exception(f"Error retrieving hotels: {str(e)}")

    @staticmethod
    def _to_dict(hotel_row):
        """Convert a hotel row from the database into a dictionary"""
        return {
            "id": hotel_row[0],
            "name": hotel_row[1],
            "address": hotel_row[2],
            "room_num": hotel_row[3],
            "location_id": hotel_row[4],
            "stars": hotel_row[5],
            "chain_id": hotel_row[6]
        }


    @staticmethod
    def insert_hotel(name, address, room_num, location_id, stars, chain_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO hotel (name, address, room_num, location_id, stars, chain_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, address, room_num, location_id, stars, chain_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting hotel: {str(e)}")
            raise Exception(f"Error inserting hotel: {str(e)}")

    @staticmethod
    def update_hotel(hotel_id, name, address, room_num, location_id, stars, chain_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE hotel
                SET name=%s, address=%s, room_num=%s, location_id=%s, stars=%s, chain_id=%s
                WHERE hotel_id=%s
            """, (name, address, room_num, location_id, stars, chain_id, hotel_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating hotel with ID {hotel_id}: {str(e)}")
            raise Exception(f"Error updating hotel with ID {hotel_id}: {str(e)}")

    @staticmethod
    def delete_hotel(hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM hotel WHERE hotel_id=%s", (hotel_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting hotel with ID {hotel_id}: {str(e)}")
            raise Exception(f"Error deleting hotel with ID {hotel_id}: {str(e)}")
