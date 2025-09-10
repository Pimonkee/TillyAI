import unittest
from src.main import app, process_input


class TillyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for Flask
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_tilly_response(self):
        # Test the /api/tilly route (updated to match blueprint prefix)
        response = self.app.post('/api/tilly', json={'text': 'Hello Tilly!'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('response', data)
        self.assertIn('Received and processed: Hello Tilly', data['response'])

    def test_process_input(self):
        # Test the process_input function
        test_text = "Apple is looking at buying U.K. startup for $1 billion."
        result = process_input(test_text)
        self.assertIn('Apple', result)
        self.assertIn('U.K.', result)
        self.assertIn('$1 billion', result)
        self.assertIn('Tokens:', result)

    def test_invalid_tilly_request(self):
        # Test invalid request to /api/tilly
        response = self.app.post('/api/tilly', json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()