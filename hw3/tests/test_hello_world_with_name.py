import unittest
from freezegun import freeze_time
from hw3.hello_world_with_name import app


class TestHelloWorldEndpoint(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2024-03-14")
    def test_hello_world_with_name_thursday(self):
        response = self.app.get('/hello-world/Alice')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alice. Хорошего четверга!', text)

    @freeze_time("2024-03-15")
    def test_hello_world_with_name_friday(self):
        response = self.app.get('/hello-world/Bob')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Bob. Хорошей пятницы!', text)

    @freeze_time("2024-03-16")
    def test_hello_world_without_name_saturday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошей субботы!', text)

    @freeze_time("2024-03-17")
    def test_hello_world_without_name_sunday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего воскресенья!', text)

    @freeze_time("2024-03-18")
    def test_hello_world_without_name_monday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего понедельника!', text)

    @freeze_time("2024-03-19")
    def test_hello_world_without_name_tuesday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего вторника!', text)

    @freeze_time("2024-03-20")
    def test_hello_world_without_name_wednesday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошей среды!', text)

    @freeze_time("2024-03-20")
    def test_hello_world_without_name_correct(self):
        response = self.app.get('/hello-world/Хорошей среды')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей среды. Хорошей среды!', text)

if __name__ == '__main__':
    unittest.main()
