from flask import Blueprint
sqlinjection = Blueprint('sqlinjection', __name__, template_folder='templates', static_folder='static')

from . import routes