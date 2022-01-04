import unittest
from lesson14.lesson14 import Unmanned


class func_test(unittest.TestCase):
    def test_road_time(self):
        self.assertEqual(Unmanned(10, 2, [[2, 2, 2], [4, 2, 2]]), 12)
        self.assertEqual(Unmanned(10, 2, [[2, 5, 3], [6, 2, 4]]), 13)
        self.assertEqual(Unmanned(15, 2, [[17, 5, 5], [20, 2, 2]]), 15)
        self.assertEqual(
            Unmanned(10, 4, [[12, 2, 2], [20, 2, 2], [22, 3, 3], [25, 2, 2]]), 10)
        self.assertEqual(Unmanned(10, 1, [[10, 5, 3]]), 10)


if __name__ == '__main__':
    unittest.main()
