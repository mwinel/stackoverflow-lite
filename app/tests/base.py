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
