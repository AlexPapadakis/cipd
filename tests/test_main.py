import unittest
from main import add_numbers, subtract_numbers

class TestMainFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)

        
