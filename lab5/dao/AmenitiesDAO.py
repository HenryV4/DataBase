from flask import current_app

class AmenitiesDAO:
    @staticmethod
    def get_all_amenities():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT amenities_id, name FROM amenities")
            rows = cursor.fetchall()
            return [AmenitiesDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving amenities: {str(e)}")
            raise Exception(f"Error retrieving amenities: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        amenities_id, name = row
        return {
            "amenities_id": amenities_id,  # лише назва таблиці + _id
            "name": name
        }

    @staticmethod
    def insert_amenity(name):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO amenities (name) VALUES (%s)", (name,))
            current_app.mysql.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            current_app.logger.error(f"Error inserting amenity: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error inserting amenity: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_amenity(amenities_id, name):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE amenities SET name=%s WHERE amenities_id=%s",
                (name, amenities_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error updating amenity {amenities_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error updating amenity {amenities_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_amenity(amenities_id):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM amenities WHERE amenities_id=%s", (amenities_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.logger.error(f"Error deleting amenity {amenities_id}: {str(e)}")
            current_app.mysql.connection.rollback()
            raise Exception(f"Error deleting amenity {amenities_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def insert_bulk():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('insert_bulk_amenities')
            current_app.mysql.connection.commit()
            return {"status": "success", "message": "Bulk amenities added successfully"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            raise Exception(f"Error inserting bulk amenities: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
