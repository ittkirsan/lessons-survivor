
import unittest
from lesson23 import TreeOfLife


class TestFunc(unittest.TestCase):

    def test_TreeOfLife(self):
        self.assertEqual(TreeOfLife(
            3, 4, 12, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])
        self.assertEqual(TreeOfLife(
            4, 4, 8, [".+..", "..+.", ".+..", '.++.']), ['.+..', '..+.', '.+..', '+++.'])
        self.assertEqual(TreeOfLife(
            4, 5, 7, [".+...", "..+..", ".+..+", '..++.']), ['+++++', '+++++', '+++++', '+++++'])
        self.assertEqual(TreeOfLife(
            3, 4, 3, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(
            4, 4, 11, [".+..", "..+.", ".+..", '....']), ['++++', '++++', '++++', '++++'])
        self.assertEqual(TreeOfLife(
            3, 4, 2, ["+..+", "+..+", "...+"]), ['....', '....', '.+..'])
        self.assertEqual(TreeOfLife(
            4, 4, 3, ["++++", "++++", "++++", '++++']), ['++++', '++++', '++++', '++++'])
        self.assertEqual(TreeOfLife(3, 4, 4, ["....", "....", "...."]), [
                         "....", "....", "...."])


if __name__ == '__main__':
    unittest.main()
