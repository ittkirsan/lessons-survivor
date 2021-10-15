
import unittest
from lesson13 import UFO


class func_test(unittest.TestCase):
    def test_basa8(self):
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])
        self.assertEqual(
            UFO(5, [1365452, 256743, 456, 7541, 12345], True), [387882, 89571, 302, 3937, 5349])
        self.assertEqual(UFO(3, [1234, 1777, 0], True), [668, 1023, 0])

    def test_basa16(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(
            UFO(5, [1365452, 256743, 456, 7541, 12345], False), [20337746, 2451267, 1110, 30017, 74565])
        self.assertEqual(UFO(3, [1234, 1777, 0], False), [4660, 6007, 0])


if __name__ == '__main__':
    unittest.main()
