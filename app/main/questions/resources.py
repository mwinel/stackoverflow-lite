import json
from flask import jsonify, request, make_response
from app.main.questions import blueprint
from app.models import Question


@blueprint.route('/questions', methods = ['POST'])
def add_question():
    Question.verifications()
    Question.add()
    return jsonify({
        'message': 'question successfully created'
    }), 201


@blueprint.route('/questions', methods = ['GET'])
def fetch_questions():
    all_questions = Question.get_all()
    return make_response(json.dumps({'questions': all_questions})), 200, \
        {'Content-Type': 'application/json'}


@blueprint.route('/questions/<int:question_id>', methods = ['GET'])
def fetch_question(question_id):
    question = Question.get_one(question_id)
    if question:
        return make_response(json.dumps({'question': question})), 200, \
            {'Content-Type': 'application/json'}
    return jsonify({'message': 'question does not exist'}), 404


@blueprint.route('/questions/<int:question_id>', methods = ['PUT'])
def update_question(question_id):
    Question.verifications()
    Question.update(question_id)
    return jsonify({'message': 'question successfully updated'}), 200


@blueprint.route('/questions/<int:question_id>', methods = ['DELETE'])
def delete_question(question_id):
    question = Question.get_one(question_id)
    if not question:
        return jsonify({'error': 'question does not exist'}), 404
    Question.delete(question_id)
    return jsonify({'message': 'question successfully deleted'}), 200
