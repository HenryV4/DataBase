# routes/routes.py
from flask import Blueprint
from controllers.RoomController import RoomController

room_bp = Blueprint('room_bp', __name__)

# CRUD Routes for rooms
@room_bp.route('/rooms', methods=['GET'])
def get_rooms():
    return RoomController.get_all_rooms()

@room_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    return RoomController.get_room(room_id)

# Route to create a new room
@room_bp.route('/rooms', methods=['POST'])
def create_room():
    return RoomController.create_room()

# Route to update an existing room
@room_bp.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    return RoomController.update_room(room_id)

# Route to delete a room
@room_bp.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    return RoomController.delete_room(room_id)
