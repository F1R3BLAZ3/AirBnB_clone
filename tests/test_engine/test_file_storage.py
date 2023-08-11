#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage.file_path):
            os.remove(self.storage.file_path)

    def test_initial_attributes(self):
        self.assertEqual(self.storage.file_path, "file.json")
        self.assertEqual(len(self.storage.all()), 0)

    def test_new_method(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertTrue(key in self.storage.all())

    def test_save_and_reload_methods(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertTrue(key in self.storage.all())

    def test_reload_method_without_file(self):
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_method_with_existing_file(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertTrue(key in self.storage.all())

if __name__ == '__main__':
    unittest.main()
