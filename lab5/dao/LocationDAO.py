from flask import current_app

class LocationDAO:
    @staticmethod
    def get_all_locations():
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT location_id, city, country FROM location")
            rows = cursor.fetchall()
            return [LocationDAO._to_dict(r) for r in rows]
        except Exception as e:
            current_app.logger.error(f"Error retrieving locations: {str(e)}")
            raise Exception(f"Error retrieving locations: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def _to_dict(row):
        """row = (location_id, city, country)"""
        location_id, city, country = row
        return {
            "location_id": location_id,   # лише <table>_id у JSON
            "city": city,
            "country": country
        }

    @staticmethod
    def get_location_by_id(location_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "SELECT location_id, city, country FROM location WHERE location_id=%s",
                (location_id,)
            )
            row = cursor.fetchone()
            return LocationDAO._to_dict(row) if row else None
        except Exception as e:
            current_app.logger.error(f"Error retrieving location {location_id}: {str(e)}")
            raise Exception(f"Error retrieving location {location_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def insert_location(city: str, country: str):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO location (city, country) VALUES (%s, %s)",
                (city, country)
            )
            current_app.mysql.connection.commit()
            return cursor.lastrowid  # новий location_id
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error inserting location: {str(e)}")
            raise Exception(f"Error inserting location: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def update_location(location_id: int, city: str, country: str):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE location SET city=%s, country=%s WHERE location_id=%s",
                (city, country, location_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error updating location {location_id}: {str(e)}")
            raise Exception(f"Error updating location {location_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass

    @staticmethod
    def delete_location(location_id: int):
        cursor = None
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "DELETE FROM location WHERE location_id=%s",
                (location_id,)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            current_app.mysql.connection.rollback()
            current_app.logger.error(f"Error deleting location {location_id}: {str(e)}")
            raise Exception(f"Error deleting location {location_id}: {str(e)}")
        finally:
            try:
                if cursor: cursor.close()
            except Exception:
                pass
