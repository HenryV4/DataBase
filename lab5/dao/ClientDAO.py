from flask import current_app

class ClientDAO:
    @staticmethod
    def get_all_clients():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT 
                    c.client_id,
                    c.full_name,
                    c.email,
                    c.phone_num,
                    c.discount_cards_id,
                    c.loyalty_program_id,
                    lp.program_name
                FROM client c
                LEFT JOIN loyalty_program lp 
                    ON c.loyalty_program_id = lp.loyalty_program_id
            """)
            rows = cursor.fetchall()
            return [ClientDAO._to_dict_with_program(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving clients: {str(e)}")
            raise Exception(f"Error retrieving clients: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict_with_program(row):
        (
            client_id,
            full_name,
            email,
            phone_num,
            discount_cards_id,
            loyalty_program_id,
            loyalty_program_name
        ) = row
        return {
            "client_id": client_id,                       # <table>_id тільки
            "full_name": full_name,
            "email": email,
            "phone_num": phone_num,
            "discount_cards_id": discount_cards_id,
            "loyalty_program_id": loyalty_program_id,     # id для POST/PUT
            "loyalty_program_name": loyalty_program_name  # зручно для UI
        }

    # ===== INSERT через звичайний SQL =====
    @staticmethod
    def insert_client_sql(full_name, email, phone_num, discount_cards_id, loyalty_program_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO client (full_name, email, phone_num, discount_cards_id, loyalty_program_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (full_name, email, phone_num, discount_cards_id, loyalty_program_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # client_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting client (SQL): {str(e)}")
            raise Exception(f"Error inserting client: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    # ===== INSERT через stored procedure =====
    # (ПЕРЕЙМЕНОВАНО, щоб не перекривати insert_client_sql)
    @staticmethod
    def insert_client_sp(full_name, email, phone_num, discount_cards_id, loyalty_program_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('insert_client', [
                full_name, email, phone_num, discount_cards_id, loyalty_program_id
            ])
            current_app.mysql.connection.commit()
            return {"status": "success", "message": "Client added successfully"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting client (SP): {str(e)}")
            raise Exception(f"Error inserting client: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_client(client_id, full_name, email, phone_num, discount_cards_id, loyalty_program_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE client
                SET full_name=%s,
                    email=%s,
                    phone_num=%s,
                    discount_cards_id=%s,
                    loyalty_program_id=%s
                WHERE client_id=%s
            """, (full_name, email, phone_num, discount_cards_id, loyalty_program_id, client_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error updating client {client_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error updating client {client_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_client(client_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM client WHERE client_id=%s", (client_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error deleting client {client_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error deleting client {client_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def get_clients_by_city(city):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT 
                    c.client_id,
                    c.full_name,
                    l.city
                FROM client c
                LEFT JOIN booking b ON c.client_id = b.client_id
                LEFT JOIN room r ON b.room_id = r.room_id
                LEFT JOIN hotel h ON r.hotel_id = h.hotel_id
                LEFT JOIN location l ON h.location_id = l.location_id
                WHERE l.city = %s
                GROUP BY c.client_id, c.full_name, l.city
            """, (city,))
            rows = cursor.fetchall()
            return [
                {"client_id": row[0], "full_name": row[1], "city": row[2]}
                for row in rows
            ]
        except Exception as e:
            current_app.logger.error(f"Error retrieving clients for city {city}: {str(e)}")
            raise Exception(f"Error retrieving clients for city {city}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
