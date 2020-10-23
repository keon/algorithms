import unittest
from algorithms.Greedy import (
    fractionalKnapsack
)


class TestfractionalKnapsack(unittest.TestCase):

    def test_get_max_value(self):
        result = fractionalKnapsack.FractionalKnapSack.get_max_value([10, 20, 30], [60, 100, 120], 50)
        self.assertEqual(result, 240.0)

    def test_get_max_value(self):
        result = fractionalKnapsack.FractionalKnapSack.get_max_value([12, 32, 33, 5, 34], [100, 200, 50, 60, 150], 50)
        self.assertEqual(result, 364.4117647058824)

    def test_get_max_value(self):
        result = fractionalKnapsack.FractionalKnapSack.get_max_value([10, 40, 20, 24], [100, 280, 120, 120], 60)
        self.assertEqual(result, 440.0)


if __name__ == "__main__":
    unittest.main()
