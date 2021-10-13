import unittest
from lesson11 import BigMinus


class func_test(unittest.TestCase):
    def test_line_coast(self):
        self.assertEqual(BigMinus("1234567891", "1"), "1234567890")
        self.assertEqual(BigMinus("1", "321"), "320")
        self.assertEqual(BigMinus("1564", "25678943"), "25677379")
        self.assertEqual(BigMinus("10000000000", "1"), "9999999999")
        self.assertEqual(BigMinus("1", "10000000000"), "9999999999")
        self.assertEqual(BigMinus("10000", "10000"), "0")
        self.assertEqual(BigMinus("0", "1"), "1")
        self.assertEqual(BigMinus("1", "1"), "0")
        self.assertEqual(BigMinus("1", "0"), "1")


if __name__ == '__main__':
    unittest.main()
