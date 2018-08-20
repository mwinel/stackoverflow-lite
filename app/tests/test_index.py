import unittest
from app.tests.base import BaseTestCase

class TestIndexCase(BaseTestCase):
    """ Test index endpoints """

    def test_index(self):
        """ Test response to the index endpoint. """
        rv = self.app.get('/api/v1/index')
        self.assertEqual(rv.status_code, 200)
		# Test a JSON response.
        self.assertEqual(rv.json, ({'message': 'Welcome to StackOverflow-Lite'}))

if __name__ == '__main__':
    unittest.main()
