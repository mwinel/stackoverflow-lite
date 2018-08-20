import json
import unittest
from app.tests.base import BaseTestCase

class TestQuestionCase(BaseTestCase):
    """ Test index endpoints """

    def test_create_question(self):
        """ Test API can create a question """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        output = json.loads(rv.data)
        self.assertTrue("question successfully created" in output["message"])


    def test_fetch_questions(self):
        """ Test API can fetch all questions """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        rv = self.app.get('/api/v1/questions', data=json.dumps(self.question),
            content_type='application/json')
        self.assertEqual(rv.status_code, 200)
        self.assertIn("Something went wrong with PyQt5 menu: GUI", str(rv.data))


    def test_fetch_a_question(self):
        """ Test API can fetch a question """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        # Test fetch for an existing question.
        resp = self.app.get('/api/v1/questions/1')
        self.assertEqual(resp.status_code, 200)
        # Test fetch for a non exiting question.
        resp = self.app.get('/api/v1/questions/30')
        self.assertEqual(resp.status_code, 404)


    def test_update_a_question(self):
        """ Test API can update a question """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        self.question = {
            "title": "Something went wrong with PyQt5 menu: GUI",
            "body": "There were something wrong when I was using \
                     PyQt5 to build a GUI window with a menu bar."
        }
        rv = self.app.put('/api/v1/questions/1', data=json.dumps(self.question), 
            content_type='application/json')
        self.assertEqual(rv.status_code, 200)
        output = json.loads(rv.data)
        self.assertTrue("question successfully updated" in output["message"])


    def test_delete_question(self):
        """ Test API can update a question """
        rv = self.app.post('/api/v1/questions', data=json.dumps(self.question2),
            content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        resp = self.app.delete('/api/v1/questions/2', data=json.dumps(self.question2),
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.app.get('/api/v1/questions/2', data=json.dumps(self.question2),
            content_type='application/json')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
