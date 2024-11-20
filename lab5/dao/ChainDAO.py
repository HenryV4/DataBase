# dao/ChainDAO.py
from flask import current_app

class ChainDAO:
    @staticmethod
    def get_all_chains():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM chain")
            chains = cursor.fetchall()
            cursor.close()
            return [ChainDAO._to_dict(chain) for chain in chains]
        except Exception as e:
            current_app.logger.error(f"Error retrieving chains: {str(e)}")
            raise Exception(f"Error retrieving chains: {str(e)}")

    @staticmethod
    def _to_dict(chain_row):
        """Convert a chain row from the database into a dictionary"""
        return {
            "id": chain_row[0],
            "name": chain_row[1]
        }


    @staticmethod
    def insert_chain(name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO chain (name) VALUES (%s)", (name,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting chain: {str(e)}")
            raise Exception(f"Error inserting chain: {str(e)}")

    @staticmethod
    def update_chain(chain_id, name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE chain SET name=%s WHERE chain_id=%s", (name, chain_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating chain with ID {chain_id}: {str(e)}")
            raise Exception(f"Error updating chain with ID {chain_id}: {str(e)}")

    @staticmethod
    def delete_chain(chain_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM chain WHERE chain_id=%s", (chain_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting chain with ID {chain_id}: {str(e)}")
            raise Exception(f"Error deleting chain with ID {chain_id}: {str(e)}")
