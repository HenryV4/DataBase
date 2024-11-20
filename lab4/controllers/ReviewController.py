# controllers/ReviewController.py
from flask import jsonify, request
from dao.ReviewDAO import ReviewDAO

class ReviewController:
    @staticmethod
    def get_all_reviews():
        try:
            reviews = ReviewDAO.get_all_reviews()
            return jsonify(reviews), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_review():
        try:
            data = request.get_json()
            ReviewDAO.insert_review(data['rating'], data.get('comment'), data['client_id'], data['hotel_id'])
            return jsonify({'message': 'Review created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_review(review_id):
        try:
            data = request.get_json()
            ReviewDAO.update_review(review_id, data['rating'], data.get('comment'), data['client_id'], data['hotel_id'])
            return jsonify({'message': 'Review updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_review(review_id):
        try:
            ReviewDAO.delete_review(review_id)
            return jsonify({'message': 'Review deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
