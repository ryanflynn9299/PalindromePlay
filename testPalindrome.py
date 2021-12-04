import unittest

from main import isPalindrome, getPalindromeAndSteps
from display_data import checkRawData


class MyTestCase(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(isPalindrome(1))
        self.assertTrue(isPalindrome(343))
        self.assertTrue(isPalindrome(1234567890987654321))
        self.assertTrue(isPalindrome(0))

    def test_notPalindrome(self):
        self.assertFalse(isPalindrome(23))
        self.assertFalse(isPalindrome(1110))
        self.assertFalse(isPalindrome(1234567890))
        self.assertFalse(isPalindrome(-1))                          # negative numbers cannot be palindromic

    def test_limit(self):
        self.assertEqual((-1, -1), getPalindromeAndSteps(196))       # default limit is 100
        self.assertEqual((-1, -1), getPalindromeAndSteps(10, steplimit=0))
        self.assertEqual((11, 1), getPalindromeAndSteps(10, steplimit=0, enforcelimit=False))

    def test_check(self):
        data1 = [(1, 1, 0), (2, 2, 0), (10, 11, 1)]         # real data
        self.assertTrue(checkRawData(data1))

        data2 = [(1, 1, 100), (2, 2, 100), (10, 11, 101)]   # correctness is not checked
        self.assertTrue(checkRawData(data2))

        data3 = [(1, -1, -1), (2, -1, -1), (10, -1, -1)]    # -1 is acceptable for error conditions
        self.assertTrue(checkRawData(data3))

        data4 = [(1, -2, 0), (2, 2, -2), (-2, 11, 1)]       # negatives cannot go in indexes 1, 2
        self.assertFalse(checkRawData(data4))

        data5 = []                                          # empty data is permissible
        self.assertTrue(checkRawData(data5))

        data6 = [(1, 1), (2, 2), (10, 11)]                  # must be 3-tuples
        self.assertFalse(checkRawData(data6))

        data7 = [(1, 1, 0), (2, 2, 0), (10, 11)]            # correction: *all* must be 3-tuples
        self.assertFalse(checkRawData(data7))

    def test_correctness(self):
        tests = [(1, 1, 0),
                 (174, 5115, 4),
                 (343, 343, 0),
                 (-100, -1, -1)]

        for inp, expPal, expSteps in tests:
            num, steps = getPalindromeAndSteps(inp)
            self.assertEqual(num, expPal, f"Expected {expPal}, got {num}")
            self.assertEqual(steps, expSteps, f"Took {steps} steps, not {expSteps}!")


if __name__ == '__main__':
    unittest.main()
