# test_app.py
import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_subtract_fail(self):
        self.assertEqual(subtract(5, 2), 1)  # Intentionally incorrect to fail

    def test_add_fail(self):
        self.assertEqual(add(2, 2), 5)  # Intentionally incorrect to fail

if __name__ == '__main__':
    unittest.main()
