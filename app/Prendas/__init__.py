from flask import Blueprint

Prendas = Blueprint('prendas', __name__, template_folder='templates')

from . import routes