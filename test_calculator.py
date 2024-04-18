import unittest
from calculator import *

class TestCal(unittest.TestCase):
    def test_sum_normal(self):
        num1 = 4
        num2 = 6
        result = addNums()
        self.assertEqual(5, result)




if __name__ == "__main__":
    unittest.main()