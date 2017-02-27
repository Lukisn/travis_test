import unittest
from stuff import add, sub, mul, div, mod, function

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.a = 3
        self.b = 4
        self.aplusb = a + b
        self.aminusb = a - b
        self.atimesb = a * b
        self.adividedbyb = a / b
        self.amodulusb = a % b

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(add(self.a, self.b), self.aplusb)

    def test_sub(self):
        self.assertEqual(sub(self.a, self.b), self.aminusb)
