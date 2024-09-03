import unittest
from src.main import app, process_input

class TillyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_tilly_response(self):
        # Test the /tilly route
        response = self.app.post('/tilly', json={'text': 'Hello Tilly!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Received Hello Tilly!', response.get_data(as_text=True))

    def test_process_input(self):
        # Test the process_input function
        test_text = "Apple is looking at buying U.K. startup for $1 billion."
        result = process_input(test_text)
        self.assertIn('Apple', result)
        self.assertIn('U.K.', result)
        self.assertIn('$1 billion', result)

if __name__ == '__main__':
    unittest.main()