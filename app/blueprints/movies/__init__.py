from flask import Blueprint

bp = Blueprint('movies', __name__, url_prefix='/')

from .import models, routes
