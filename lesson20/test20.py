import unittest
from lesson20 import BastShoe


class TestFunc(unittest.TestCase):

    def test_BastShoe(self):
        self.assertEqual(BastShoe('1 Привет'), 'Привет')
        self.assertEqual(BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(BastShoe('2 2'), 'Привет, Мир!')

        self.assertEqual(BastShoe('4'), 'Привет, Мир!++')
        self.assertEqual(BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(BastShoe('1 *'), 'Привет, Мир!*')
        self.assertEqual(BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(BastShoe('3 6'), ',')
        self.assertEqual(BastShoe('2 100'), '')
        self.assertEqual(BastShoe('5'), '')
        self.assertEqual(BastShoe('1 a'), 'a')
        self.assertEqual(BastShoe('1 s'), 'as')
        self.assertEqual(BastShoe('1 d'), 'asd')
        self.assertEqual(BastShoe('4'), 'as')
        self.assertEqual(BastShoe('4'), 'a')
        self.assertEqual(BastShoe('5'), 'as')


if __name__ == '__main__':
    unittest.main()
