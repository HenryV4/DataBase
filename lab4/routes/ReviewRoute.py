# routes/ReviewRoute.py
from flask import Blueprint
from controllers.ReviewController import ReviewController

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    return ReviewController.get_all_reviews()

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    return ReviewController.create_review()

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return ReviewController.update_review(review_id)

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return ReviewController.delete_review(review_id)
