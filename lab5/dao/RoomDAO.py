# dao/RoomDAO.py
from flask import current_app

class RoomDAO:
    @staticmethod
    def get_all_rooms():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM room")  # Querying the room table
            rooms = cursor.fetchall()  # Fetching results
            cursor.close()
            
            # Convert each row (tuple) to a dictionary
            room_list = []
            for room in rooms:
                room_dict = {
                    'id': room[0],
                    'room_type': room[1],
                    'price_per_night': room[2],
                    'available': room[3],
                    'hotel_id': room[4]
                }
                room_list.append(room_dict)

            return room_list
        except Exception as e:
            current_app.logger.error(f"Error retrieving rooms: {str(e)}")
            raise Exception(f"Error retrieving rooms: {str(e)}")

    @staticmethod
    def get_room_by_id(room_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM room WHERE id = %s", (room_id,))
            room = cursor.fetchone()
            cursor.close()

            if room:
                # Convert the tuple to a dictionary
                room_dict = {
                    'id': room[0],
                    'room_type': room[1],
                    'price_per_night': room[2],
                    'available': room[3],
                    'hotel_id': room[4]
                }
                return room_dict
            return None
        except Exception as e:
            current_app.logger.error(f"Error retrieving room with ID {room_id}: {str(e)}")
            raise Exception(f"Error retrieving room with ID {room_id}: {str(e)}")
        
    @staticmethod
    def get_all_rooms_for_hotel(hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM room WHERE hotel_id=%s", (hotel_id,))
            rooms = cursor.fetchall()
            cursor.close()
            return rooms
        except Exception as e:
            current_app.logger.error(f"Error retrieving rooms for hotel {hotel_id}: {str(e)}")
            raise Exception(f"Error retrieving rooms for hotel {hotel_id}: {str(e)}")

    @staticmethod
    def insert_room(room_type, price_per_night, available, hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO room (room_type, price_per_night, available, hotel_id)
                VALUES (%s, %s, %s, %s)
            """, (room_type, price_per_night, available, hotel_id))
            current_app.mysql.connection.commit()
            room_id = cursor.lastrowid
            cursor.close()
            return room_id
        except Exception as e:
            current_app.logger.error(f"Error inserting room: {str(e)}")
            raise Exception(f"Error inserting room: {str(e)}")

    @staticmethod
    def update_room(room_id, room_type, price_per_night, available, hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE room
                SET room_type = %s, price_per_night = %s, available = %s, hotel_id = %s
                WHERE room_id = %s
            """, (room_type, price_per_night, available, hotel_id, room_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating room with ID {room_id}: {str(e)}")
            raise Exception(f"Error updating room with ID {room_id}: {str(e)}")

    @staticmethod
    def delete_room(room_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM room WHERE room_id = %s", (room_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting room with ID {room_id}: {str(e)}")
            raise Exception(f"Error deleting room with ID {room_id}: {str(e)}")
