import unittest

def calculate_area(length, width):
    return length * width

class TestCalculateArea(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_area(3, 4), 12)
        self.assertEqual(calculate_area(5, 5), 25)

    def test_zero(self):
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(10, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(calculate_area(-3, 4), -12)
        self.assertEqual(calculate_area(3, -4), -12)
        self.assertEqual(calculate_area(-3, -4), 12)

    def test_float_numbers(self):
        self.assertAlmostEqual(calculate_area(2.5, 3.5), 8.75)
        self.assertAlmostEqual(calculate_area(0.1, 0.1), 0.01)

    def test_large_numbers(self):
        self.assertEqual(calculate_area(1000000, 1000000), 1000000000000)

if __name__ == '__main__':
    unittest.main()