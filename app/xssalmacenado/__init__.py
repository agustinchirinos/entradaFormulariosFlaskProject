from flask import Blueprint
xssalmacenado = Blueprint('xssalmacenado', __name__, template_folder='templates', static_folder='static')

from . import routes