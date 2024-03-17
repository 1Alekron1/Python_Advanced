import unittest
from hw3.decrypt import decrypt


class TestDecryptor(unittest.TestCase):

    def test_decrypt_single_dot(self):
        with self.subTest(case="Single Dot"):
            encrypted_text = "абра-кад.абра"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "абра-кадабра")

    def test_decrypt_double_dots(self):
        with self.subTest(case="Double Dots"):
            encrypted_text = "абраа..-кадабра"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "абра-кадабра")

    def test_decrypt_mix_dots(self):
        with self.subTest(case="Mix Dots"):
            encrypted_text = "абраа..-.кадабра"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "абра-кадабра")

    def test_decrypt_multiple_dashes(self):
        with self.subTest(case="Multiple Dashes"):
            encrypted_text = "абра--..кадабра"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "абра-кадабра")

    def test_decrypt_extra_dots(self):
        with self.subTest(case="Extra Dots"):
            encrypted_text = "абрау...-кадабра"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "абра-кадабра")

    def test_decrypt_all_dots(self):
        with self.subTest(case="All Dots"):
            encrypted_text = "абра........"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "")

    def test_decrypt_extra_characters(self):
        with self.subTest(case="Extra Characters"):
            encrypted_text = "абр......a."
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "a")

    def test_decrypt_digits(self):
        with self.subTest(case="Digits"):
            encrypted_text = "1..2.3"
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "23")

    def test_decrypt_only_dot(self):
        with self.subTest(case="Only Dot"):
            encrypted_text = "."
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "")

    def test_decrypt_multiple_dots(self):
        with self.subTest(case="Multiple Dots"):
            encrypted_text = "1......................."
            decrypted_text = decrypt(encrypted_text)
            self.assertEqual(decrypted_text, "")


if __name__ == '__main__':
    unittest.main()
