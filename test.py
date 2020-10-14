import unittest
import numpy as np
from mult import mult


class TestDot(unittest.TestCase):
    def test1(self):
        n = 3
        a = np.ones((n, n))
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertTrue(mult(a, b) == np.dot(a, b))

    def test2(self):
        a = 1010
        b = 12

        self.assertTrue(mult(a, b) == np.dot(a, b))

    def test3(self):
        a = [1, 2, 3, 4]
        b = [5, 6, 7, 8]

        self.assertTrue(mult(a, b) == np.dot(a, b))
        

if __name__ == '__main__':
    unittest.main()
