import unittest
from lesson15 import TankRush


class func_test(unittest.TestCase):
    def TankRunsh(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(
            TankRush(3, 4, "1234 5674 0987", 2, 2, "34 98"), False)
        self.assertEqual(TankRush(3, 4, "1234 4567 7890", 2, 2, "34 67"), True)
        self.assertEqual(
            TankRush(3, 4, "1234 5647 8901", 2, 2, "12 01"), False)
        self.assertEqual(
            TankRush(4, 6, '578914 123456 045782 458792', 3, 3, '914 222 782'), True)
        self.assertEqual(
            TankRush(4, 6, '578914 123456 045782 458792', 3, 3, '914 456 782'), False)
        self.assertEqual(
            TankRush(4, 6, '578914 123456 045782 458792', 2, 2, '87 92'), False)


if __name__ == '__main__':
    unittest.main()
