from flask import Blueprint
from controllers.DistributeDataController import DistributeDataController

distribute_data_bp = Blueprint('distribute_data', __name__)

@distribute_data_bp.route('/random', methods=['POST'])
def distribute_data_randomly():
    return DistributeDataController.distribute_data_randomly()
