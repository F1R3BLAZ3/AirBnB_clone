#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_attributes(self):
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(my_model_dict["name"], "My First Model")
        self.assertEqual(my_model_dict["my_number"], 89)

if __name__ == "__main__":
    unittest.main()
