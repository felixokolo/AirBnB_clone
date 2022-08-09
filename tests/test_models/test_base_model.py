#!/usr/bin/python3
"""Unittest module"""

import unittest
import sys
import io

sys.path.insert(0, 'models')
Base = __import__('base_model').BaseModel
Rectangle = __import__('rectangle').Rectangle


class BaseModelTest(unittest.TestCase):
    """Test class for base model"""

    def test_base_class(self):
        """test unit for base class
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)


    def test_rectangle_class(self):
        """test unit for base class
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


    def test_rectangle_val(self):
        """test unit for base class
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


    def test_rectangle_val(self):
        """test unit for rectangle area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


    def test_rectangle_disp(self):
        """test unit for rectangle print
        """
        capOut = io.StringIO()
        sys.stdout = capOut
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("####\n####\n####\n####\n####\n####\n",
                            capOut.getvalue())
        capOut.close()
        capOut = io.StringIO()
        sys.stdout = capOut
        r2 = Rectangle(2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("##\n##\n",
                            capOut.getvalue())
        capOut.close()


    def test_rectangle_print(self):
        """test unit for rectangle print
        """
        capOut = io.StringIO()
        sys.stdout = capOut
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6\n",
                            capOut.getvalue())
        capOut.close()
        capOut = io.StringIO()
        sys.stdout = capOut
        r2 = Rectangle(5, 5, 1)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] (9) 1/0 - 5/5\n",
                            capOut.getvalue())
        capOut.close()


if __name__ == '__main__':
    unittest.main()