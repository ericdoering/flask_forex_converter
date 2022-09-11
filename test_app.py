import app
from unittest import TestCase


class ConverterTestCases(TestCase):
    """Testing Flask App"""

    def test_currency(self):
        """Testing that when currency A is 0 currency B should be 0"""
        self.assertEqual(self.currA == 0, self.currB == 0)
    

    def test_submission_form(self):
        """Testing that route works and has a response of 200"""
        with app.test_client() as client:
            resp = client.get('/')

            self.assertEqual(resp.status_code, 200)

