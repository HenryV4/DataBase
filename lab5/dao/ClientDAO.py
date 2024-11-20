# dao/ClientDAO.py

from flask import current_app, jsonify, request

class ClientDAO:
    @staticmethod
    def get_all_clients():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM client")
            clients = cursor.fetchall()
            cursor.close()
            return [ClientDAO._to_dict(client) for client in clients]
        except Exception as e:
            current_app.logger.error(f"Error retrieving clients: {str(e)}")
            raise Exception(f"Error retrieving clients: {str(e)}")

    @staticmethod
    def _to_dict(client_row):
        """Convert a client row from the database into a dictionary"""
        return {
            "id": client_row[0],
            "full_name": client_row[1],
            "email": client_row[2],
            "phone_num": client_row[3],
            "discount_cards_id": client_row[4]
        }


    @staticmethod
    def insert_client(full_name, email, phone_num, discount_cards_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO client (full_name, email, phone_num, discount_cards_id) VALUES (%s, %s, %s, %s)",
                           (full_name, email, phone_num, discount_cards_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting client: {str(e)}")
            raise Exception(f"Error inserting client: {str(e)}")

    @staticmethod
    def update_client(client_id, full_name, email, phone_num, discount_cards_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE client SET full_name=%s, email=%s, phone_num=%s, discount_cards_id=%s WHERE client_id=%s",
                           (full_name, email, phone_num, discount_cards_id, client_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating client with ID {client_id}: {str(e)}")
            raise Exception(f"Error updating client with ID {client_id}: {str(e)}")

    @staticmethod
    def delete_client(client_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM client WHERE client_id=%s", (client_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting client with ID {client_id}: {str(e)}")
            raise Exception(f"Error deleting client with ID {client_id}: {str(e)}")

    @staticmethod
    def get_clients_by_city(city):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT c.full_name, l.city
                FROM client c
                LEFT JOIN booking b ON c.id = b.client_id
                LEFT JOIN room r ON b.room_id = r.id
                LEFT JOIN hotel h ON r.hotel_id = h.id
                LEFT JOIN location l ON h.location_id = l.id
                WHERE l.city = %s
            """, (city,))
            clients = cursor.fetchall()
            cursor.close()
            return clients
        except Exception as e:
            current_app.logger.error(f"Error retrieving clients for city {city}: {str(e)}")
            raise Exception(f"Error retrieving clients for city {city}: {str(e)}")

    @staticmethod
    def insert_client(full_name, email, phone_num, discount_cards_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('insert_client', [full_name, email, phone_num, discount_cards_id])
            current_app.mysql.connection.commit()
            cursor.close()
            return {"status": "success", "message": "Client added successfully"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting client: {str(e)}")
            raise Exception(f"Error inserting client: {str(e)}")

    @staticmethod
    def get_stat():
        """Calls the calculate_stat stored procedure to get a statistical value"""
        try:
            table_name = request.json.get('table')
            column_name = request.json.get('column')
            operation = request.json.get('operation')

            if not table_name or not column_name or not operation:
                raise ValueError("Table name, column name, and operation must be provided")

            result = ClientDAO.calculate_stat(table_name, column_name, operation)
            return jsonify(result), 200
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def calculate_stat(table_name, column_name, operation):
        try:
            cursor = current_app.mysql.connection.cursor()

            cursor.callproc('calculate_stat', [table_name, column_name, operation])

            result = cursor.fetchone()

            current_app.logger.debug(f"Raw database output: {result}")

            if result and len(result) > 0 and result[0] is not None:
                return {"status": "success", "result": result[0]}
            else:
                return {"status": "error", "message": "Result is NULL or not returned"}
        except Exception as e:
            current_app.logger.error(f"Error calculating stat: {str(e)}")
            raise Exception(f"Error calculating stat: {str(e)}")
        finally:
            if cursor:
                cursor.close()

