import unittest

def armstrong_szam(num: int):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

class TestFunctions(unittest.TestCase):
    def test_armstrong_szam()