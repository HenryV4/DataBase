# dao/ReviewDAO.py
from flask import current_app

class ReviewDAO:
    @staticmethod
    def get_all_reviews():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM review")
            reviews = cursor.fetchall()
            cursor.close()
            return [ReviewDAO._to_dict(review) for review in reviews]
        except Exception as e:
            current_app.logger.error(f"Error retrieving reviews: {str(e)}")
            raise Exception(f"Error retrieving reviews: {str(e)}")

    @staticmethod
    def _to_dict(review_row):
        """Convert a review row from the database into a dictionary"""
        return {
            "id": review_row[0],
            "rating": review_row[1],
            "comment": review_row[2],
            "client_id": review_row[3],
            "hotel_id": review_row[4]
        }


    @staticmethod
    def insert_review(rating, comment, client_id, hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO review (rating, comment, client_id, hotel_id) VALUES (%s, %s, %s, %s)",
                           (rating, comment, client_id, hotel_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting review: {str(e)}")
            raise Exception(f"Error inserting review: {str(e)}")

    @staticmethod
    def update_review(review_id, rating, comment, client_id, hotel_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE review SET rating=%s, comment=%s, client_id=%s, hotel_id=%s WHERE review_id=%s",
                           (rating, comment, client_id, hotel_id, review_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating review with ID {review_id}: {str(e)}")
            raise Exception(f"Error updating review with ID {review_id}: {str(e)}")

    @staticmethod
    def delete_review(review_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM review WHERE review_id=%s", (review_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting review with ID {review_id}: {str(e)}")
            raise Exception(f"Error deleting review with ID {review_id}: {str(e)}")
