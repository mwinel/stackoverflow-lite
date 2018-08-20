from flask_testing import TestCase
from manage import app

class BaseTestCase(TestCase):
    """ Base Tests. """

    def create_app(self):
        """ Returns app. """
        return app
    
    def setUp(self):
        """ Create test database and set up test client. """
        self.app = app.test_client()
        # Add some questions
        self.question = {
            "title": "Something went wrong with PyQt5 menu: GUI",
            "body": "There was something that wrong when I was using \
                    PyQt5 to build a GUI window with a menu bar."
        }
        self.question2 = {
            "title": "ImportError: Can not import app from name 'app'",
            "body": "I found this error when I tried to execute my code \
                    from the flask-mega-tutorial."
        }
