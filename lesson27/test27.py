import unittest
from lesson27 import Football


class testFunc(unittest.TestCase):

    def test_Football(self):
        self.assertEqual(Football([1, 3, 2], 3), True)
        self.assertEqual(Football([3, 2, 1], 3), True)
        self.assertEqual(Football([1, 7, 5, 3, 9], 5), True)
        self.assertEqual(Football([9, 5, 3, 7, 1], 5), False)
        self.assertEqual(Football([1, 4, 3, 2, 5], 5), True)
        self.assertEqual(Football([5, 3], 2), True)
        self.assertEqual(Football([1, 2, 6, 5, 4, 3, 7, 8], 8), True)
        self.assertEqual(Football([1, 2, 5, 3, 4], 5), False)
        self.assertAlmostEqual(Football([5], 1), False)
        self.assertAlmostEqual(Football([1, 2, 3], 3), False)


if __name__ == '__main__':
    unittest.main()
