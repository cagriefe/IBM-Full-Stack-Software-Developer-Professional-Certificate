import unittest

from mymodule import square, double, add

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4.0), 16.0)
    
class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3), 6)
        self.assertEqual(double(4.0), 8.0)
    
class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(4.0, 5.0), 9.0)
        self.assertEqual(add(3.21, 4.32), 7.53)
unittest.main()