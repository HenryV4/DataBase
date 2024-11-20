# dao/PaymentDAO.py
from flask import current_app

class PaymentDAO:
    @staticmethod
    def get_all_payments():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM payment")
            payments = cursor.fetchall()
            cursor.close()
            return [PaymentDAO._to_dict(payment) for payment in payments]
        except Exception as e:
            current_app.logger.error(f"Error retrieving payments: {str(e)}")
            raise Exception(f"Error retrieving payments: {str(e)}")

    @staticmethod
    def _to_dict(payment_row):
        """Convert a payment row from the database into a dictionary"""
        return {
            "id": payment_row[0],
            "card_number": payment_row[1],
            "payment_amount": str(payment_row[2]),
            "payment_date": str(payment_row[3]),
            "status": payment_row[4],
            "client_id": payment_row[5]
        }


    @staticmethod
    def insert_payment(card_number, payment_amount, payment_date, status, client_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO payment (card_number, payment_amount, payment_date, status, client_id) VALUES (%s, %s, %s, %s, %s)",
                           (card_number, payment_amount, payment_date, status, client_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting payment: {str(e)}")
            raise Exception(f"Error inserting payment: {str(e)}")

    @staticmethod
    def update_payment(payment_id, card_number, payment_amount, payment_date, status, client_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE payment SET card_number=%s, payment_amount=%s, payment_date=%s, status=%s, client_id=%s WHERE payment_id=%s",
                           (card_number, payment_amount, payment_date, status, client_id, payment_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating payment with ID {payment_id}: {str(e)}")
            raise Exception(f"Error updating payment with ID {payment_id}: {str(e)}")

    @staticmethod
    def delete_payment(payment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM payment WHERE payment_id=%s", (payment_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting payment with ID {payment_id}: {str(e)}")
            raise Exception(f"Error deleting payment with ID {payment_id}: {str(e)}")
