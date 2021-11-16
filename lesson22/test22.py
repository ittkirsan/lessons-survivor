import unittest
from lesson22 import SherlockValidString


class TestFunc(unittest.TestCase):

    def test_SherlockValidString(self):
        self.assertEqual(SherlockValidString('xyz'), True)
        self.assertEqual(SherlockValidString('xyzaa'), True)
        self.assertEqual(SherlockValidString('xxyyz'), True)
        self.assertEqual(SherlockValidString('xxyyz'), True)
        self.assertEqual(SherlockValidString('xxyyza'), False)
        self.assertEqual(SherlockValidString('xxyyzabc'), False),
        self.assertEqual(SherlockValidString('xxxyyyzzz'), True)
        self.assertEqual(SherlockValidString('zzzyyyzzzz'), False)
        self.assertEqual(SherlockValidString('asdfghjkll'), True)
        self.assertEqual(SherlockValidString('aaassssdddd'), False)
        self.assertEqual(SherlockValidString('asasasffff'), True)
        self.assertEqual(SherlockValidString('asasasfffff'), False)
        self.assertEqual(SherlockValidString('qwwwwwwz'), False)
        self.assertEqual(SherlockValidString('xyzvbnjkm'), True)


if __name__ == '__main__':
    unittest.main()
