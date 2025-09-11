from flask import jsonify, request
from dao.ChainDAO import ChainDAO

class ChainController:
    @staticmethod
    def get_all_chains():
        try:
            chains = ChainDAO.get_all_chains()
            return jsonify(chains), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_chain():
        try:
            data = request.get_json()
            ChainDAO.insert_chain(data['name'])
            return jsonify({'message': 'Chain created successfully!'}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_chain(chain_id):
        try:
            data = request.get_json()
            ChainDAO.update_chain(chain_id, data['name'])
            return jsonify({'message': 'Chain updated successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_chain(chain_id):
        try:
            ChainDAO.delete_chain(chain_id)
            return jsonify({'message': 'Chain deleted successfully!'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
