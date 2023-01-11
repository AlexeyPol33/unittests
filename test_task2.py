import task2
import unittest

class TestTask2 (unittest.TestCase):
    def setUp(self) -> None:
        self.real_token = task2.ya_disk('') # Настоящий токен яндекс диска
        self.wrong_token = task2.ya_disk  ('y0_LgAbHADKOoTzAADLWwZZZZDP1XgQ8RkZKwl4TpiuwsVaAQtOcC459DA')
        self.None_token = task2.ya_disk  (None)

    def test_connection (self):
        self.assertEqual(self.real_token.get_info().status_code,200)
        self.assertNotEqual(self.wrong_token.get_info().status_code,200)
        self.assertNotEqual(self.None_token.get_info().status_code,200)

    def test_create_folder (self):
        self.assertEqual(self.real_token.create_folder('test3333').status_code,201)
        self.real_token.del_folder('test3333')
        self.assertNotEqual(self.wrong_token.create_folder('test3333').status_code,201)
        self.assertNotEqual(self.None_token.create_folder('test3333').status_code,201)

if __name__ == '__main__':
    unittest.main()

