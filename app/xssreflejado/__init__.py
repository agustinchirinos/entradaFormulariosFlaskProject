from flask import Blueprint
xssreflejado = Blueprint('xssreflejado', __name__, template_folder='templates', static_folder='static')

from . import routes
