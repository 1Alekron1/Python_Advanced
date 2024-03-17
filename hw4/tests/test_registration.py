import unittest
from hw4.registration import app


class TestRegistration(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_valid_registration(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_registration(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '',  # Empty phone number
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_email(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_invalid_email_format(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'invalid_email',
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_phone(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_invalid_phone_length(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '12345',  # Invalid phone number length
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_invalid_phone_format(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': 'abcdef',  # Invalid phone number format
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_name(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'address': '123 Main St',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_address(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'name': 'John Doe',
                'index': '12345',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_index(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_missing_comment(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': '12345',
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_index_type(self):
        with app.test_request_context('/registration', method='POST'):
            data = {
                'email': 'test@example.com',
                'phone': '1234567890',
                'name': 'John Doe',
                'address': '123 Main St',
                'index': 'invalid_index',  # Invalid index type
                'comment': 'This is a test comment'
            }
            response = self.app.post('/registration', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)


if __name__ == '__main__':
    unittest.main()
