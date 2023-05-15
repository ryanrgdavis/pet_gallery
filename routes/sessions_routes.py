from flask import Blueprint
from controllers.sessions_controller import new, add, delete

sessions_routes = Blueprint('sessions_routes', __name__)

sessions_routes.route('/new')(new)
sessions_routes.route('', methods=["POST"])(add)
sessions_routes.route('/delete', methods=["POST"])(delete)