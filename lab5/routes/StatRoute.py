from flask import Blueprint
from ..controllers.StatController import StatController

stat_bp = Blueprint('stat', __name__)

@stat_bp.route('/calculate', methods=['POST'])
def get_stat():
    return StatController.get_stat()
