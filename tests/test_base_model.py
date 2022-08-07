import unittest
from models.base_model import BaseModel

class Test_base_model(unittest.TestCase):
    '''
    Test cases for the instance attribute of id
    '''
    def test_instanceAttributes(self):
        #instantiate the baseModel class
        base = BaseModel()
        base2 = BaseModel()

        #Tests the id attributes
        self.assertIsInstance(base2,BaseModel)
        self.assertTrue(hasattr(base2,"id"))
        self.assertTrue(hasattr(base2,"name"))
        self.assertTrue(hasattr(base2,"my_number"))
        self.assertNotEqual(base,base2)
        self.assertIsInstance(base.id,str)

    # def test_c(self):
    #     base = BaseModel()
    #     base2 = BaseModel()
    #     self.assertEqual(base2,str(base))

    # def test_id(self):
    #     base = BaseModel()
    #     base2 = BaseModel()
    #     self.assertIsInstance(base2,BaseModel)
    #     self.assertTrue(hasattr(base2,"id"))
    #     self.assertTrue(hasattr(base2,"name"))
    #     self.assertTrue(hasattr(base2,"my_number"))
    #     self.assertNotEqual(base,base2)
    #     self.assertIsInstance(base.id,str)


