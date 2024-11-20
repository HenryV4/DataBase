# controllers/PaymentController.py
from flask import jsonify, request
from dao.PaymentDAO import PaymentDAO

class PaymentController:
    @staticmethod
    def get_all_payments():
        try:
            payments = PaymentDAO.get_all_payments()
            return jsonify(payments), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_payment():
        try:
            data = request.get_json()
            PaymentDAO.insert_payment(data['card_number'], data['payment_amount'], data['payment_date'], data['status'], data['client_id'])
            return jsonify({'message': 'Payment created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_payment(payment_id):
        try:
            data = request.get_json()
            PaymentDAO.update_payment(payment_id, data['card_number'], data['payment_amount'], data['payment_date'], data['status'], data['client_id'])
            return jsonify({'message': 'Payment updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_payment(payment_id):
        try:
            PaymentDAO.delete_payment(payment_id)
            return jsonify({'message': 'Payment deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
