import unittest
from Q1_code import dfa_accepts_101
from Q3_code import binary_divisible_by_3

class TestAutomataFunctions(unittest.TestCase):

    # Tests for Q1_code (contains '101')
    def test_dfa_accepts_101_valid(self):
        self.assertTrue(dfa_accepts_101("110101"))
        self.assertTrue(dfa_accepts_101("101"))
        self.assertFalse(dfa_accepts_101("11111"))
        self.assertFalse(dfa_accepts_101("000"))

    def test_dfa_accepts_101_invalid_input(self):
        self.assertEqual(dfa_accepts_101("10a1"), "Error: Please enter a valid binary string (only 0 and 1).")

    # Tests for Q3_code (divisible by 3)
    def test_binary_divisible_by_3_valid(self):
        self.assertTrue(binary_divisible_by_3("0"))       # 0
        self.assertTrue(binary_divisible_by_3("11"))      # 3
        self.assertTrue(binary_divisible_by_3("110"))     # 6
        self.assertFalse(binary_divisible_by_3("10"))     # 2
        self.assertTrue(binary_divisible_by_3("1001"))   # 9 is divisible by 3

    def test_binary_divisible_by_3_invalid_input(self):
        self.assertEqual(binary_divisible_by_3("10a1"), "Error: Please enter a valid binary number (only 0 and 1).")

if __name__ == '__main__':
    unittest.main()