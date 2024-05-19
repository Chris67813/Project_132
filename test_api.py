import unittest
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import create_app, db
from flask import current_app
from flask_testing import TestCase

class BasicTests(TestCase):
    def create_app(self):
        # Pass in test configuration
        app = create_app('testing')
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        # Add any other setup needed for tests

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_rps_game_page(self):
        response = self.client.get('/rpsgame')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Rock Paper Scissors', response.data)

    def test_login(self):
        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have been logged out', response.data)

    def test_registration(self):
        response = self.client.post('/register', data=dict(
            username='newuser',
            email='newuser@example.com',
            password='password123',
            confirm='password123'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)

    def test_nft_shop_page(self):
        response = self.client.get('/shop')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'NFT Shop', response.data)

    def test_quiz_game_page(self):
        response = self.client.get('/quiz')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Quiz Game', response.data)

    def test_coin_game_page(self):
        response = self.client.get('/CoinGame')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Coin Game', response.data)

    def test_snake_game_page(self):
        response = self.client.get('/SnakeGame')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Snake Game', response.data)

    def test_top_global_page(self):
        response = self.client.get('/rank')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Top Global', response.data)

if __name__ == '__main__':
    unittest.main()
