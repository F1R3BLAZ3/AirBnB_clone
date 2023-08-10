import unittest
from models import storage
from models.base_model import BaseModel

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = storage

    def test_reloaded_objects(self):
        all_objs = self.storage.all()
        self.assertTrue(len(all_objs) >= 0)  # Adjust this as needed
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsInstance(obj, BaseModel)

    def test_create_new_object(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        obj_id = my_model.id
        retrieved_obj = self.storage.get("BaseModel", obj_id)
        self.assertIsInstance(retrieved_obj, BaseModel)
        self.assertEqual(retrieved_obj.name, "My_First_Model")
        self.assertEqual(retrieved_obj.my_number, 89)

if __name__ == "__main__":
    unittest.main()
