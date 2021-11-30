import unittest
from lesson24 import MatrixTurn


class TestFunc(unittest.TestCase):
    def test_MatrixTurn(self):
        self.assertEqual(MatrixTurn(['123456', '234567', '345678', '456789'], 4, 6, 1), [
                         '212345', '343456', '456767', '567898'])
        self.assertEqual(MatrixTurn(['123456', '234567', '345678', '456789'], 4, 6, 3), [
                         '432123', '565434', '676545', '789876'])
        self.assertEqual(MatrixTurn(['555', '789'], 2, 3, 1), ['755', '895'])
        self.assertEqual(MatrixTurn(['555', '789'], 2, 3, 5), ['559', '578'])
        self.assertEqual(MatrixTurn(['000000', '111111', '222222', '333333', '444444', '555555'], 6, 6, 1), [
                         '100000', '221110', '333211', '443222', '544433', '555554'])
        self.assertEqual(MatrixTurn(['000000', '111111', '222222', '333333', '444444', '555555'], 6, 6, 3), [
                         '321000', '443210', '542310', '542310', '543211', '555432'])


if __name__ == '__main__':
    unittest.main()
