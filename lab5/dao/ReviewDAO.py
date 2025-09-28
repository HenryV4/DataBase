from flask import current_app

class ReviewDAO:
    @staticmethod
    def get_all_reviews():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT review_id, rating, comment, client_id, hotel_id
                FROM review
            """)
            rows = cursor.fetchall()
            return [ReviewDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving reviews: {str(e)}")
            raise Exception(f"Error retrieving reviews: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """
        row = (review_id, rating, comment, client_id, hotel_id)
        """
        review_id, rating, comment, client_id, hotel_id = row
        return {
            "review_id": review_id,       # тільки <table>_id у JSON
            "rating": int(rating) if rating is not None else None,
            "comment": comment,
            "client_id": client_id,
            "hotel_id": hotel_id
        }

    @staticmethod
    def insert_review(rating, comment, client_id, hotel_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO review (rating, comment, client_id, hotel_id)
                VALUES (%s, %s, %s, %s)
            """, (rating, comment, client_id, hotel_id))
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # новий review_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting review: {str(e)}")
            raise Exception(f"Error inserting review: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_review(review_id, rating, comment, client_id, hotel_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE review
                SET rating=%s,
                    comment=%s,
                    client_id=%s,
                    hotel_id=%s
                WHERE review_id=%s
            """, (rating, comment, client_id, hotel_id, review_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating review {review_id}: {str(e)}")
            raise Exception(f"Error updating review {review_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_review(review_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM review WHERE review_id=%s", (review_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting review {review_id}: {str(e)}")
            raise Exception(f"Error deleting review {review_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
