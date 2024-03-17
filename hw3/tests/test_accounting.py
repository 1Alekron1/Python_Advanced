import unittest
from hw3.accounting import app


class TestFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.storage = {
            2022: {
                1: {
                    1: 100,
                    2: 150
                },
                'total': 250
            }
        }
    


    def test_add_expense(self):
        response = self.app.get('/add/20220103/50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Затраты добавлены.')

    def test_calculate_year(self):
        response = self.app.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Суммарные траты за 2022 год: 300')

    def test_calculate_month(self):
        response = self.app.get('/calculate/2022/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Суммарные траты за 1.2022: 300')

    def test_invalid_date_format(self):
        response = self.app.get('/add/202201/50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Неверный формат даты')

    def test_empty_storage_year(self):
        response = self.app.get('/calculate/2023')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Нет данных о затратах за указанный год.')

    def test_empty_storage_month(self):
        response = self.app.get('/calculate/2022/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Нет данных о затратах за указанный месяц.')


if __name__ == '__main__':
    unittest.main()
