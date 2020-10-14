import unittest
import numpy as np
from mult import mult


class TestDot(unittest.TestCase):
    def test1(self):
        n = 3
        a = np.zeros((n, n), dtype=int)
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        c = mult(a, b) == np.dot(a, b)

        self.assertTrue(c.all())

    def test2(self):
        a = 1010
        b = 12
        c = mult(a, b) == np.dot(a, b)

        self.assertTrue(c.all())

    def test3(self):
        a = [1, 2, 3, 4]
        b = [5, 6, 7, 8]
        c = mult(a, b) == np.dot(a, b)

        self.assertTrue(c.all())
        

if __name__ == '__main__':
    unittest.main()
