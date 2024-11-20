# controllers/RoomController.py
from flask import jsonify, request
from ..dao.RoomDAO import RoomDAO

class RoomController:
    @staticmethod
    def get_all_rooms():
        try:
            rooms = RoomDAO.get_all_rooms()
            return jsonify(rooms), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_room(room_id):
        try:
            room = RoomDAO.get_room_by_id(room_id)
            if room:
                return jsonify(room), 200
            return jsonify({"message": "Room not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_room():
        try:
            data = request.get_json()
            room_id = RoomDAO.insert_room(
                data['room_type'],
                data['price_per_night'],
                data['available'],
                data['hotel_id']
            )
            return jsonify({"id": room_id, "message": "Room created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_room(room_id):
        try:
            data = request.get_json()
            room = RoomDAO.get_room_by_id(room_id)
            if not room:
                return jsonify({"message": "Room not found"}), 404
            RoomDAO.update_room(
                room_id,
                data['room_type'],
                data['price_per_night'],
                data['available'],
                data['hotel_id']
            )
            return jsonify({"message": "Room updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_room(room_id):
        try:
            room = RoomDAO.get_room_by_id(room_id)
            if not room:
                return jsonify({"message": "Room not found"}), 404
            RoomDAO.delete_room(room_id)
            return jsonify({"message": "Room deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
