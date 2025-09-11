from flask import Blueprint
from controllers.DiscountCardController import DiscountCardController

discount_card_bp = Blueprint('discount_card_bp', __name__)

@discount_card_bp.route('/discount_cards', methods=['GET'])
def get_discount_cards():
    return DiscountCardController.get_all_discount_cards()

@discount_card_bp.route('/discount_cards', methods=['POST'])
def create_discount_card():
    return DiscountCardController.create_discount_card()

@discount_card_bp.route('/discount_cards/<int:card_id>', methods=['PUT'])
def update_discount_card(card_id):
    return DiscountCardController.update_discount_card(card_id)

@discount_card_bp.route('/discount_cards/<int:card_id>', methods=['DELETE'])
def delete_discount_card(card_id):
    return DiscountCardController.delete_discount_card(card_id)
