

import tut21_calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(tut21_calc.add(5, 10), 15)
        self.assertEqual(tut21_calc.add(-5, 10), 5)
        self.assertEqual(tut21_calc.add(-5, -10), -15)
        self.assertEqual(tut21_calc.add(5.25, 100.15), 105.40)

    def test_sub(self):
        self.assertEqual(tut21_calc.sub(5, 6), -1)
        self.assertEqual(tut21_calc.sub(5, -6), 11)
        self.assertEqual(tut21_calc.sub(-5, 6), -11)
        self.assertEqual(tut21_calc.sub(32.57, 12.43), 20.14)

    def test_mul(self):
        self.assertEqual(tut21_calc.mul(2, 5), 10)
        self.assertEqual(tut21_calc.mul(2, -5), -10)
        self.assertEqual(tut21_calc.mul(-2, -5), 10)
        self.assertEqual(tut21_calc.mul(-2.5, -5), 12.5)

    def test_div(self):
        self.assertEqual(tut21_calc.div(10, 2), 5)

        with self.assertRaises(ValueError):
            tut21_calc.div(10, 0)



if __name__ == '__main__':
    unittest.main()

