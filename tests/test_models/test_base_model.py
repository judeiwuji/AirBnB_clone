#!/usr/bin/python3
"""
Contains basemodel test cases.
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    test class for basemodel class
    """

    def setUP(self):
        pass

    def test_instance(self):
        """obj should be a BaseModel instance"""

        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertFalse(b1 is b2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        b1 = BaseModel()
        my_model_dict = b1.to_dict()
        b2 = BaseModel(**my_model_dict)
        self.assertEqual(b1.id, b2.id)

    def test_save(self):
        """test save method"""
        b1 = BaseModel()
        old = b1.updated_at
        b1.save()
        self.assertFalse(old == b1.updated_at)

    def test_str(self):
        """test the __str__ majic method"""
        pass


if __name__ == "__main__":
    unittest.main(TestBaseModel)
