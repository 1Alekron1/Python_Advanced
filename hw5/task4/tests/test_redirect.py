import unittest
import sys
from io import StringIO
from hw5.task4.redirect import Redirect


class TestRedirect(unittest.TestCase):
    def test_redirect_stdout(self):
        stdout_file = StringIO()
        with Redirect(stdout=stdout_file):
            print('Hello redirected stdout')
        stdout_file.seek(0)
        self.assertEqual(stdout_file.read().strip(), 'Hello redirected stdout')

    def test_redirect_stderr(self):
        stderr_file = StringIO()
        with Redirect(stderr=stderr_file):
            print('Hello redirected stderr', file=sys.stderr)
        stderr_file.seek(0)
        self.assertEqual(stderr_file.read().strip(), 'Hello redirected stderr')

    def test_redirect_stdout_and_stderr(self):
        stdout_file = StringIO()
        stderr_file = StringIO()
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello redirected stdout')
            print('Hello redirected stderr', file=sys.stderr)
        stdout_file.seek(0)
        stderr_file.seek(0)
        self.assertEqual(stdout_file.read().strip(), 'Hello redirected stdout')
        self.assertEqual(stderr_file.read().strip(), 'Hello redirected stderr')

    def test_redirect_stdout_restore(self):
        old_stdout = sys.stdout
        stdout_file = StringIO()
        with Redirect(stdout=stdout_file):
            print('Hello redirected stdout')
        self.assertEqual(sys.stdout, old_stdout)

    def test_redirect_stderr_restore(self):
        old_stderr = sys.stderr
        stderr_file = StringIO()
        with Redirect(stderr=stderr_file):
            print('Hello redirected stderr', file=sys.stderr)
        self.assertEqual(sys.stderr, old_stderr)

    def test_redirect_stdout_and_stderr_restore(self):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        stdout_file = StringIO()
        stderr_file = StringIO()
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello redirected stdout')
            print('Hello redirected stderr', file=sys.stderr)
        self.assertEqual(sys.stdout, old_stdout)
        self.assertEqual(sys.stderr, old_stderr)

    def test_no_arguments(self):
        # Сохраняем текущие потоки вывода
        old_stdout = sys.stdout
        old_stderr = sys.stderr

        # Создаем объекты StringIO для перенаправления вывода
        new_stdout = StringIO()
        new_stderr = StringIO()

        # Запускаем блок с контекстным менеджером без аргументов
        with Redirect():
            # Пишем в стандартные потоки вывода
            print("Hello stdout")
            print("Hello stderr", file=sys.stderr)

        # Проверяем, что вывод был перенаправлен в новые потоки
        self.assertEqual(new_stdout.getvalue(), "")
        self.assertEqual(new_stderr.getvalue(), "")

        # Восстанавливаем стандартные потоки вывода
        sys.stdout = old_stdout
        sys.stderr = old_stderr


if __name__ == '__main__':
    unittest.main()
