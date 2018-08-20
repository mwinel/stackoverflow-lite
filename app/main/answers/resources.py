from flask import jsonify, request
from app.main.answers import blueprint
from app.models import Question, Answer, questions


@blueprint.route('/questions/<int:question_id>/answers', methods = ['POST'])
def add_answer(question_id):
    for question in questions:
        if question['id'] == question_id:
            data = request.get_json()
            body = data['body']
            if body.strip() == "":
                return jsonify({'error': 'Body is missing'}), 400
            if len(body.strip()) < 30:
                return jsonify({'error': 'Body must be atleast 15 characters'}), 400
            Answer.add()
            return jsonify({'message': 'answer successfully added'}), 201
