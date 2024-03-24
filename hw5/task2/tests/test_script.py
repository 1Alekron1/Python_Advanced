import unittest
from hw5.task2.script import app

import json

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_valid_input(self):
        response = self.app.post('/execute', data={'code': 'a=2', 'timeout': 5})
        data = response.get_json()
        self.assertIn('result', data)

    def test_invalid_input(self):
        data = json.dumps({'timeout': 5})
        response = self.app.post('/execute', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_timeout(self):
        data = json.dumps({'code': 'import time\nwhile True:\n    time.sleep(1)', 'timeout': 2})
        response = self.app.post('/execute', data=data, content_type='application/json')
        data = response.get_json()
        self.assertIn('error', data)

    def test_shell_injection(self):
        data = json.dumps({'code': 'print("Hacked!")"; echo "hacked', 'timeout': 5})
        response = self.app.post('/execute', data=data, content_type='application/json')
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()