import unittest
from lesson10 import PrintingCosts


class func_test(unittest.TestCase):
    def test_line_coast(self):
        self.assertEqual(PrintingCosts("!z FG$"), 102)
        self.assertEqual(PrintingCosts("ййййй"), 5*23)
        self.assertEqual(PrintingCosts(";:.,"), 30)
        self.assertEqual(PrintingCosts(";:.,ппп"), 99)


if __name__ == '__main__':
    unittest.main()
