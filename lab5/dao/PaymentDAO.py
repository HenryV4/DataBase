from flask import current_app

class PaymentDAO:
    @staticmethod
    def get_all_payments():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT payment_id, card_number, payment_amount, payment_date, status, client_id
                FROM payment
            """)
            rows = cursor.fetchall()
            return [PaymentDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving payments: {str(e)}")
            raise Exception(f"Error retrieving payments: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """
        row = (payment_id, card_number, payment_amount, payment_date, status, client_id)
        """
        payment_id, card_number, amount, pay_date, status, client_id = row
        return {
            "payment_id": payment_id,                                   # лише <table>_id у JSON
            "card_number": card_number,
            "payment_amount": float(amount) if amount is not None else None,
            "payment_date": str(pay_date) if pay_date is not None else None,
            "status": status,
            "client_id": client_id
        }

    @staticmethod
    def insert_payment(card_number, payment_amount, payment_date, status, client_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO payment (card_number, payment_amount, payment_date, status, client_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (card_number, payment_amount, payment_date, status, client_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # новий payment_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting payment: {str(e)}")
            raise Exception(f"Error inserting payment: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_payment(payment_id, card_number, payment_amount, payment_date, status, client_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE payment
                SET card_number=%s,
                    payment_amount=%s,
                    payment_date=%s,
                    status=%s,
                    client_id=%s
                WHERE payment_id=%s
            """, (card_number, payment_amount, payment_date, status, client_id, payment_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating payment {payment_id}: {str(e)}")
            raise Exception(f"Error updating payment {payment_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_payment(payment_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM payment WHERE payment_id=%s", (payment_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting payment {payment_id}: {str(e)}")
            raise Exception(f"Error deleting payment {payment_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
