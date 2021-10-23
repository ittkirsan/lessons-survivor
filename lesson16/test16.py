

import unittest
from lesson16 import MaximumDiscount


class func_test(unittest.TestCase):
    def MaximumDiscount(self):
        self.assertEqual(MaximumDiscount(
            7, [300, 350, 400, 250, 200, 150, 100]), 450)
        self.assertEqual(MaximumDiscount(
            2, [300, 350]), 0)
        self.assertEqual(MaximumDiscount(3, [300, 50, 200]), 50)
        self.assertEqual(MaximumDiscount(
            10, [300, 350, 400, 250, 100, 100, 100, 50, 550, 20]), 500)


if __name__ == '__main__':
    unittest.main()
