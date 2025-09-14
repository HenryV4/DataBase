from flask import current_app, jsonify, request

class ClientHotelDAO:
    @staticmethod
    def insert_relation(client_name, hotel_name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('insert_client_hotel_relation', [client_name, hotel_name])
            current_app.mysql.connection.commit()
            cursor.close()
            return {"status": "success", "message": "Client-Hotel relation added successfully"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            return {"status": "error", "message": str(e)}  # Передати помилку в API-відповідь

