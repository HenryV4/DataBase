# routes/ChainRoute.py
from flask import Blueprint
from controllers.ChainController import ChainController

chain_bp = Blueprint('chain_bp', __name__)

@chain_bp.route('/chains', methods=['GET'])
def get_chains():
    return ChainController.get_all_chains()

@chain_bp.route('/chains/<int:chain_id>', methods=['GET'])
def get_chain(chain_id):
    return ChainController.get_chain(chain_id)

@chain_bp.route('/chains', methods=['POST'])
def create_chain():
    return ChainController.create_chain()

@chain_bp.route('/chains/<int:chain_id>', methods=['PUT'])
def update_chain(chain_id):
    return ChainController.update_chain(chain_id)

@chain_bp.route('/chains/<int:chain_id>', methods=['DELETE'])
def delete_chain(chain_id):
    return ChainController.delete_chain(chain_id)
