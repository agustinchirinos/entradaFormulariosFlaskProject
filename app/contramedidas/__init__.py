from flask import Blueprint
contramedidas = Blueprint('contramedidas', __name__, template_folder='templates', static_folder='static')

from . import routes, forms
