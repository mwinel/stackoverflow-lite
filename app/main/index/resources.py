from flask import jsonify
from app.main.index import blueprint

@blueprint.route('/')
@blueprint.route('/index')
def index():
    return jsonify({'message': 'Welcome to StackOverflow-Lite'}), 200