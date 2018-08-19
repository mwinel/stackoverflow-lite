from flask import jsonify, request, abort

# Initialize a questions list
questions = []

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