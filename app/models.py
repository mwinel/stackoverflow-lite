from flask import jsonify, request

# Initialize a questions list
questions = []
# Initialize the answers list
answers = []

# Define a class Question
class Question:
    
    # Constructor to create class objects
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body

    @staticmethod
    def add():
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

    @staticmethod
    def get_all():
        return questions

    @classmethod
    def get_one(cls, question_id):
        return [question for question in questions if question['id'] == question_id]

    @classmethod
    def update(cls, question_id):
        question = [x for x in questions if x['id'] == question_id]
        question[0]["title"] = request.json.get("title", question[0]["title"])
        question[0]['body'] = request.json.get('body', question[0]['body'])

    @staticmethod
    def delete(question_id):
        for i, request in enumerate(questions):
            if request.get("id") == question_id:
                del questions[i]
                break

    @staticmethod
    def verifications():
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


class Answer:

    def __init__(self, id, body):
        self.id = id
        self.body = body

    @staticmethod
    def add():
        answers = {
            'id': id,
            'body': request.json['body']
        }
        questions.append(answers)
        