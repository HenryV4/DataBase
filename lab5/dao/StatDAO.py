from flask import current_app

class StatDAO:
    @staticmethod
    def calculate_stat(table_name, column_name, operation):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('calculate_stat', [table_name, column_name, operation])
            result = cursor.fetchone()
            cursor.close()

            if result and len(result) > 0 and result[0] is not None:
                return {"status": "success", "result": result[0]}
            else:
                return {"status": "error", "message": "Result is NULL or not returned"}
        except Exception as e:
            raise Exception(f"Error calculating stat: {str(e)}")
