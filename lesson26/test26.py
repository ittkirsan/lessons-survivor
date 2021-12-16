
import unittest
from lesson26 import white_walkers


class testFunc(unittest.TestCase):
    def test_walkers(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)
        self.assertEqual(white_walkers("5==ooooooo=5=5"), False)
        self.assertEqual(white_walkers("abc=7==hdjs=3gg1=======5"), True)
        self.assertEqual(white_walkers("aaS=8"), False)
        self.assertEqual(white_walkers("9===1===9===1===9"), True)
        self.assertEqual(white_walkers("axcgb6===4xfaf5===kl6"), True)
        self.assertEqual(white_walkers("6==4"), False)
        self.assertEqual(white_walkers("6====4"), False)
        self.assertEqual(white_walkers("asda6===4dsfsdf"), True)
        self.assertEqual(white_walkers("6===4"), True)
        self.assertEqual(white_walkers(
            "6sad===4asd===fds5===sad6==sd=4"), True)
        self.assertEqual(white_walkers(""), False)
        self.assertEqual(white_walkers("9=1===9===1===9"), False)
        self.assertEqual(white_walkers("9===1===9===1====9"), False)


if __name__ == '__main__':
    unittest.main()
