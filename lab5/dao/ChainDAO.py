from flask import current_app

class ChainDAO:
    @staticmethod
    def get_all_chains():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT chain_id, name FROM chain")
            rows = cursor.fetchall()
            return [ChainDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving chains: {str(e)}")
            raise Exception(f"Error retrieving chains: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(chain_row):
        chain_id, name = chain_row
        return {
            "chain_id": chain_id,  # лише назва таблиці + _id
            "name": name
        }

    @staticmethod
    def insert_chain(name):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO chain (name) VALUES (%s)", (name,))
            current_app.mysql.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            current_app.logger.error(f"Error inserting chain: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error inserting chain: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_chain(chain_id, name):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE chain SET name=%s WHERE chain_id=%s",
                (name, chain_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error updating chain {chain_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error updating chain {chain_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_chain(chain_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM chain WHERE chain_id=%s", (chain_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error deleting chain {chain_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error deleting chain {chain_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
