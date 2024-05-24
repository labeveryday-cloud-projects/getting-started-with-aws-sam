# tests/my_lambda.py
import unittest
from my_lambda import app


class TestMyLambdaFunction(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or mocks
        self.event = {
            # Sample event data
        }
        self.context = {}

    def test_lambda_handler(self):
        response = app.lambda_handler(self.event, self.context)
        self.assertEqual(response["statusCode"], 200)
        # Add more assertions as needed

if __name__ == "__main__":
    unittest.main()