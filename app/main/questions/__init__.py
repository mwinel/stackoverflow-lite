from flask import Blueprint

blueprint = Blueprint('questions', __name__)

from app.main.questions import resources
