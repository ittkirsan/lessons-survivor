import unittest
from lesson21 import BiggerGreater


class TestFunc(unittest.TestCase):

    def test_BiggerGreater(self):
        self.assertEqual(BiggerGreater('ая'), 'яа')
        self.assertEqual(BiggerGreater('fffff'), '')
        self.assertEqual(BiggerGreater('нклм'), 'нкмл')
        self.assertEqual(BiggerGreater('вибк'), 'викб')
        self.assertEqual(BiggerGreater('вкиб'), 'ибвк')
        self.assertEqual(BiggerGreater('мояпрелесть'), 'мояпрелесьт')
        self.assertEqual(BiggerGreater('алохомора'), 'алохомрао')
        self.assertEqual(BiggerGreater('авадакедавра'), 'авадакедарав')
        self.assertEqual(BiggerGreater('sonorus'), 'sonosru')
        self.assertEqual(BiggerGreater('confundo'), 'confunod')
        self.assertEqual(BiggerGreater('expectopatronum'), 'expectopatroumn')
        self.assertEqual(BiggerGreater('экспеллиармус'), 'экспеллиарсму')


if __name__ == '__main__':
    unittest.main()
