import unittest
from stuff import add, sub, mul, div, mod, function


class TestStuff(unittest.TestCase):

    def setUp(self):
        self.a = 3
        self.b = 4
        self.aplusb = self.a +self.b
        self.aminusb = self.a - self.b
        self.atimesb = self.a * self.b
        self.adividedbyb = self.a / self.b
        self.amodulusb = self.a % self.b

    def test_add(self):
        self.assertEqual(add(self.a, self.b), self.aplusb)

    def test_sub(self):
        self.assertEqual(sub(self.a, self.b), self.aminusb)

    def test_mul(self):
        self.assertEqual(mul(self.a, self.b), self.atimesb)

    def test_div(self):
        self.assertEqual(div(self.a, self.b), self.adividedbyb)

    def test_mod(self):
        self.assertEqual(mod(self.a, self.b), self.amodulusb)

    def test_function(self):
        self.assertEqual(function(self.a, self.b, add), self.aplusb)
        self.assertEqual(function(self.a, self.b, sub), self.aminusb)
        self.assertEqual(function(self.a, self.b, mul), self.atimesb)
        self.assertEqual(function(self.a, self.b, div), self.adividedbyb)
        self.assertEqual(function(self.a, self.b, mod), self.amodulusb)

if __name__ == "__main__":
    unittest.main()
