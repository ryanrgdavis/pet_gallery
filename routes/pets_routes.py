from flask import Blueprint
from controllers.pets_controller import index, new, add, edit, delete, comment, update, show

pets_routes = Blueprint('pets_routes', __name__)

pets_routes.route('/')(index)
pets_routes.route('/new')(new)
pets_routes.route('', methods=['POST'])(add)
pets_routes.route('/<pet_id>/edit', methods=['GET'])(edit)
pets_routes.route('/<pet_id>/', methods=['POST'])(update)
pets_routes.route('/<pet_id>/delete', methods=['POST'])(delete)
pets_routes.route('/<pet_id>/comments', methods=['POST'])(comment)
# pets_routes.route("/<pet_id>/", methods=['POST'])(toggle_comment)
pets_routes.route('/<int:pet_id>/show', methods=['GET'])(show)