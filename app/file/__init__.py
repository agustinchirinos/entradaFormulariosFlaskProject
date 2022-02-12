from flask import Blueprint
file = Blueprint('file', __name__, template_folder='templates', static_folder='static')

from . import routes
