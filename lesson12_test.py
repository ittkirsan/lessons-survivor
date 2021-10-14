
import unittest
from lesson12 import MassVote


class func_test(unittest.TestCase):
    def test_line_coast(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), "majority winner 1")
        self.assertEqual(MassVote(3, [10, 15, 10]), "minority winner 2")
        self.assertEqual(MassVote(4, [111, 111, 110, 110]), "no winner")
        self.assertEqual(MassVote(5, [10, 10, 15, 60, 5]), "majority winner 4")
        self.assertEqual(
            MassVote(6, [15, 101, 110, 110, 110, 25]), "no winner")
        self.assertEqual(
            MassVote(5, [10, 15, 10, 25, 11]), "minority winner 4")


if __name__ == '__main__':
    unittest.main()
