import unittest
from hw5.task3.BlockErrors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_ignore_error(self):
        with BlockErrors({ZeroDivisionError}):
            a = 1 / 0
            print("Executed without errors")

    def test_propagate_error(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_inner_block_ignore(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                with BlockErrors({TypeError}):
                    a = 1 / '0'
                print("Inner block: executed without errors")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_ignore_child_errors(self):
        try:
            with BlockErrors({Exception}):
                a = 1 / '0'
                print("Executed without errors")
        except Exception as e:
            self.fail("An unexpected exception was raised")


if __name__ == '__main__':
    unittest.main()
