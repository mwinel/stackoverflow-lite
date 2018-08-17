import json
import unittest
from app.tests.base import BaseTestCase

class TestQuestionCase(BaseTestCase):
    """ Test index endpoints """

    def test_create_question(self):
        """ Test API can create a question. """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        output = json.loads(rv.data)
        self.assertTrue("question successfully created" in output["message"])

if __name__ == '__main__':
    unittest.main()
