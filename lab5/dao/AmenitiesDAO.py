from flask import current_app

class AmenitiesDAO:
    @staticmethod
    def get_all_amenities():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM amenities")
            amenities = cursor.fetchall()
            cursor.close()
            return [AmenitiesDAO._to_dict(amenity) for amenity in amenities]
        except Exception as e:
            current_app.logger.error(f"Error retrieving amenities: {str(e)}")
            raise Exception(f"Error retrieving amenities: {str(e)}")

    @staticmethod
    def _to_dict(amenity_row):
        """Convert an amenity row from the database into a dictionary"""
        return {
            "id": amenity_row[0],
            "name": amenity_row[1]
        }


    @staticmethod
    def insert_amenity(name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO amenities (name) VALUES (%s)", (name,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting amenity: {str(e)}")
            raise Exception(f"Error inserting amenity: {str(e)}")

    @staticmethod
    def update_amenity(amenity_id, name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE amenities SET name=%s WHERE amenity_id=%s", (name, amenity_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating amenity with ID {amenity_id}: {str(e)}")
            raise Exception(f"Error updating amenity with ID {amenity_id}: {str(e)}")

    @staticmethod
    def delete_amenity(amenity_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM amenities WHERE amenity_id=%s", (amenity_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting amenity with ID {amenity_id}: {str(e)}")
            raise Exception(f"Error deleting amenity with ID {amenity_id}: {str(e)}")

    @staticmethod
    def insert_bulk():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('insert_bulk_amenities')
            current_app.mysql.connection.commit()
            cursor.close()
            return {"status": "success", "message": "Bulk amenities added successfully"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            raise Exception(f"Error inserting bulk amenities: {str(e)}")