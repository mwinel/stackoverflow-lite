import json
from flask import jsonify, request, make_response
from app.main.questions import blueprint
from app.models import Question


@blueprint.route('/questions', methods = ['POST'])
def add_question():
    data = request.get_json()
    title = data['title']
    body = data['body']
    if title.strip() == "":
        return jsonify({'error': 'Title is missing'}), 400
    if len(title.strip()) < 15:
        return jsonify({'error': 'Title must be atleast 15 characters'}), 400
    if body.strip() == "":
        return jsonify({'error': 'Body is missing'}), 400
    if len(body.strip()) < 30:
        return jsonify({'error': 'Body must be atleast 15 characters'}), 400
    Question.add()
    return jsonify({
        'message': 'question successfully created'
    }), 201


@blueprint.route('/questions', methods = ['GET'])
def fetch_questions():
    all_questions = Question.get_all()
    return make_response(json.dumps({'questions': all_questions})), 200, \
        {'Content-Type': 'application/json'}
