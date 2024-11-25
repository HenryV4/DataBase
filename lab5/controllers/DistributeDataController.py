from flask import jsonify
from ..dao.DistributeDataDAO import DistributeDataDAO

class DistributeDataController:
    @staticmethod
    def distribute_data_randomly():
        try:
            result = DistributeDataDAO.distribute_randomly()
            return jsonify(result), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
