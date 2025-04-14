import flask_app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode(), 'Hi! from actions')

if __name__ == '__main__':
    unittest.main()