
import unittest
from lesson17 import LineAnalysis


class TestFunc(unittest.TestCase):
    def test_LineAnalysis(self):
        self.assertEqual(LineAnalysis('*..*..*..*..*..*..*'), True)
        self.assertEqual(LineAnalysis('*'), True)
        self.assertEqual(LineAnalysis('***'), True)
        self.assertEqual(LineAnalysis('*.......*.......*'), True)
        self.assertEqual(LineAnalysis('**'), True)
        self.assertEqual(LineAnalysis('*.*'), True)
        self.assertEqual(LineAnalysis('*..*...*..*..*..*..*'), False)
        self.assertEqual(LineAnalysis('*..*..*..*..*..**..*'), False)
        self.assertEqual(LineAnalysis('**********.*'), False)
        self.assertEqual(LineAnalysis('*...........*'), True)
        self.assertEqual(LineAnalysis(''), True)


if __name__ == '__main__':
    unittest.main()
