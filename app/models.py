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
