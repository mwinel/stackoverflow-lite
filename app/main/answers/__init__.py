from flask import Blueprint

blueprint = Blueprint('answers', __name__)

from app.main.answers import resources
