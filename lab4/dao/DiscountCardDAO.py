# dao/DiscountCardDAO.py
from flask import current_app

class DiscountCardDAO:
    @staticmethod
    def get_all_discount_cards():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM discount_cards")
            cards = cursor.fetchall()
            cursor.close()
            return [DiscountCardDAO._to_dict(card) for card in cards]
        except Exception as e:
            current_app.logger.error(f"Error retrieving discount cards: {str(e)}")
            raise Exception(f"Error retrieving discount cards: {str(e)}")

    @staticmethod
    def _to_dict(card_row):
        """Convert a discount card row from the database into a dictionary"""
        return {
            "id": card_row[0],
            "name": card_row[1],
            "discount": card_row[2]
        }


    @staticmethod
    def insert_discount_card(name, discount):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO discount_cards (name, discount) VALUES (%s, %s)", (name, discount))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting discount card: {str(e)}")
            raise Exception(f"Error inserting discount card: {str(e)}")

    @staticmethod
    def update_discount_card(card_id, name, discount):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE discount_cards SET name=%s, discount=%s WHERE id=%s", (name, discount, card_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating discount card with ID {card_id}: {str(e)}")
            raise Exception(f"Error updating discount card with ID {card_id}: {str(e)}")

    @staticmethod
    def delete_discount_card(card_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM discount_cards WHERE id=%s", (card_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting discount card with ID {card_id}: {str(e)}")
            raise Exception(f"Error deleting discount card with ID {card_id}: {str(e)}")
