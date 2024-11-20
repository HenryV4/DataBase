# controllers/DiscountCardController.py
from flask import jsonify, request
from ..dao.DiscountCardDAO import DiscountCardDAO

class DiscountCardController:
    @staticmethod
    def get_all_discount_cards():
        try:
            cards = DiscountCardDAO.get_all_discount_cards()
            return jsonify(cards), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_discount_card():
        try:
            data = request.get_json()
            DiscountCardDAO.insert_discount_card(data['name'], data['discount'])
            return jsonify({'message': 'Discount card created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_discount_card(card_id):
        try:
            data = request.get_json()
            DiscountCardDAO.update_discount_card(card_id, data['name'], data['discount'])
            return jsonify({'message': 'Discount card updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_discount_card(card_id):
        try:
            DiscountCardDAO.delete_discount_card(card_id)
            return jsonify({'message': 'Discount card deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
