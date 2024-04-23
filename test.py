import unittest
from solution import sortExpressions


class TestSolution(unittest.TestCase):
    test_data: list = [
        (["x = y + 6", "y = 7 * 4", "z = ( x * y )"],
         ["y = 7 * 4", "x = y + 6", "z = ( x * y )"]),
        (["x = a * y", "y = x * 5"],
         ["cyclic_dependency"]),
    ]

    def test_sortExpressions(self):
        for data in TestSolution.test_data:
            self.assertEqual(sortExpressions(data[0]), data[1])


if __name__ == '__main__':
    unittest.main()
