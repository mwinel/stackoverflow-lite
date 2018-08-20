from flask import Blueprint

blueprint = Blueprint('index', __name__)

from app.main.index import resources
