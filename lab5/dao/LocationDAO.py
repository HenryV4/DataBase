from flask import current_app

class LocationDAO:
    @staticmethod
    def get_all_locations():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM location")
            locations = cursor.fetchall()
            cursor.close()
            return [LocationDAO._to_dict(location) for location in locations]
        except Exception as e:
            current_app.logger.error(f"Error retrieving locations: {str(e)}")
            raise Exception(f"Error retrieving locations: {str(e)}")

    @staticmethod
    def _to_dict(location_row):
        """Convert a location row from the database into a dictionary"""
        return {
            "id": location_row[0],
            "city": location_row[1],
            "country": location_row[2]
        }


    @staticmethod
    def get_location_by_id(location_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM location WHERE id = %s", (location_id,))
            location = cursor.fetchone()  # Fetches one record
            cursor.close()
            return location  # Returns a single location record
        except Exception as e:
            current_app.logger.error(f"Error retrieving location with ID {location_id}: {str(e)}")
            raise Exception(f"Error retrieving location with ID {location_id}: {str(e)}")

    @staticmethod
    def insert_location(city, country):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO location (city, country) VALUES (%s, %s)", (city, country))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error inserting location: {str(e)}")
            raise Exception(f"Error inserting location: {str(e)}")

    @staticmethod
    def update_location(location_id, city, country):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE location SET city=%s, country=%s WHERE location_id=%s", (city, country, location_id))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error updating location with ID {location_id}: {str(e)}")
            raise Exception(f"Error updating location with ID {location_id}: {str(e)}")

    @staticmethod
    def delete_location(location_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM location WHERE location_id=%s", (location_id,))
            current_app.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            current_app.logger.error(f"Error deleting location with ID {location_id}: {str(e)}")
            raise Exception(f"Error deleting location with ID {location_id}: {str(e)}")
