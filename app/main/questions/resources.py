import json
from flask import jsonify, request, make_response
from app.main.questions import blueprint
from app.models import Question

# Initialize a questions list
questions = []

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
    global id
    if len(questions) == 0:
        id = len(questions) + 1
    else:
        id = id + 1
    question = {
        'id': id,
        'title': request.json['title'],
        'body': request.json['body']
    }
    questions.append(question)
    return jsonify({
        'message': 'question successfully created'
    }), 201

@blueprint.route('/questions', methods = ['GET'])
def fetch_questions():
    return make_response(json.dumps({'questions': questions})), 200, \
        {'Content-Type': 'application/json'}

@blueprint.route('/questions/<int:question_id>', methods = ['GET'])
def get_question(question_id):
    for question in questions:
        if question['id'] == question_id:            
            resp = {
                'id': question['id'],
                'title': question['title'],
                'body': question['body']
            }
            return make_response(json.dumps(resp)), 200, \
                {'Content-Type': 'application/json'}
    return jsonify({'message': 'question does not exist'}), 404

@blueprint.route('/questions/<int:question_id>', methods = ['PUT'])
def update_question(question_id):
    # Find and return a question matching a specific Id.
    question = [x for x in questions if x['id'] == question_id]
    # Set update conditions.
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
    # Update a question
    question[0]["title"] = request.json.get("title", question[0]["title"])
    question[0]['body'] = request.json.get('body', question[0]['body'])
    return jsonify({'message': 'question successfully updated'}), 200

@blueprint.route('/questions/<int:question_id>', methods = ['DELETE'])
def delete_question(question_id):
    question = [x for x in questions if x['id'] == question_id]
    if not question:
        return jsonify({'error': 'question does not exist'}), 404
    questions.remove(question[0])
    return jsonify({'message': 'question successfully deleted'}), 200
