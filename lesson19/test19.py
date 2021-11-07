
import unittest
from lesson19 import ShopOLAP


class TestFunc(unittest.TestCase):
    def test_ShopOLAP(self):
        self.assertEqual(ShopOLAP(5, ["платье1 5", "сумка32 2", "платье1 1", "сумка23 2", "сумка128 4"]),
                         ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])
        self.assertEqual(ShopOLAP(5, ["платье1 1", "платье1 2", "платье1 3", "платье1 4", "платье1 5"]),
                         ['платье1 15'])
        self.assertEqual(ShopOLAP(5, ["платье1 5", "платье12 5", "платье123 1", "платье12 5", "платье123 5"]),
                         ['платье12 10', "платье123 6", "платье1 5"])
        self.assertEqual(ShopOLAP(2, ["платье1 5", "платье12 5"]), [
                         "платье1 5", "платье12 5"])


if __name__ == '__main__':
    unittest.main()
