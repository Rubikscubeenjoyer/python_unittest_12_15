import unittest

def armstrong_szam(num: int):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

class TestFunctions(unittest.TestCase):
    def test_armstrong_szam(self):
        self.assertTrue(armstrong_szam(153))
        self.assertFalse(armstrong_szam(123))

if __name__ == "__main__":
    unittest.main()