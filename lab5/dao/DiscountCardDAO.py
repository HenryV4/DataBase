from flask import current_app

class DiscountCardDAO:
    @staticmethod
    def get_all_discount_cards():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                SELECT discount_cards_id, name, discount
                FROM discount_cards
            """)
            rows = cursor.fetchall()
            return [DiscountCardDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving discount cards: {str(e)}")
            raise Exception(f"Error retrieving discount cards: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        discount_cards_id, name, discount = row
        return {
            "discount_cards_id": discount_cards_id,   # тільки <table>_id у JSON
            "name": name,
            "discount": float(discount) if discount is not None else None
        }

    @staticmethod
    def insert_discount_card(name, discount):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO discount_cards (name, discount) VALUES (%s, %s)",
                (name, discount)
            )
            current_app.mysql.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting discount card: {str(e)}")
            raise Exception(f"Error inserting discount card: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_discount_card(discount_cards_id, name, discount):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                UPDATE discount_cards
                SET name=%s, discount=%s
                WHERE discount_cards_id=%s
            """, (name, discount, discount_cards_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating discount card {discount_cards_id}: {str(e)}")
            raise Exception(f"Error updating discount card {discount_cards_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_discount_card(discount_cards_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "DELETE FROM discount_cards WHERE discount_cards_id=%s",
                (discount_cards_id,)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting discount card {discount_cards_id}: {str(e)}")
            raise Exception(f"Error deleting discount card {discount_cards_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
