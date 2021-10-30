
import unittest
from lesson18 import MisterRobot


class testFunc(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]), True)
        self.assertEqual(MisterRobot(
            10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), False)
        self.assertEqual(MisterRobot(4, [4, 3, 2, 1]), True)
        self.assertEqual(MisterRobot(4, [1, 2, 4, 3]), False)
        self.assertEqual(MisterRobot(5, [5, 2, 4, 1, 3]), False)
        self.assertEqual(MisterRobot(7, [7, 6, 5, 4, 3, 2, 1]), False)


if __name__ == '__main__':
    unittest.main()
