from flask import Blueprint
from controllers.pets_controller import index, new, add, edit, delete, like

pets_routes = Blueprint('pets_routes', __name__)

pets_routes.route('/')(index)
pets_routes.route('/new')(new)
pets_routes.route('', methods=['POST'])(add)
pets_routes.route('/<id>/edit')(edit)
pets_routes.route('/<id>/delete', methods=["POST"])(delete)
pets_routes.route('/<id>/likes', methods=["POST"])(like)