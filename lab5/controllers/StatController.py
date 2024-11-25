from flask import request, jsonify
from ..dao.StatDAO import StatDAO

class StatController:
    @staticmethod
    def get_stat():
        try:
            data = request.get_json()
            table_name = data.get('table')
            column_name = data.get('column')
            operation = data.get('operation')

            if not table_name:
                return jsonify({"error": "Table name is required"}), 400
            if not column_name:
                return jsonify({"error": "Column name is required"}), 400
            if operation not in ['MAX', 'MIN', 'SUM', 'AVG']:
                return jsonify({"error": "Invalid operation. Allowed: MAX, MIN, SUM, AVG"}), 400

            result = StatDAO.calculate_stat(table_name, column_name, operation)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
