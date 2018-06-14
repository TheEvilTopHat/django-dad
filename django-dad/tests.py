from django.test import TestCase
import requests

# Create your tests here.


class DadJokeTestCase(TestCase):
    def test_dad_joke_connection(self):
            """tests if it can reach dad joke website (https://icanhazdadjoke.com/)"""
            r = requests.get('https://icanhazdadjoke.com/',headers={'Accept': 'text/plain'})
            self.assertEqual(r.status_code, 200)
