import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.storage._FileStorage__objects = {}

    def test_new_method(self):
        self.storage.new(self.model)
        self.assertIn(
            f"{self.model.__class__.__name__}.{self.model.id}",
            self.storage.all()
        )

    def test_save_method(self):
        self.storage.new(self.model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn(
            f"{self.model.__class__.__name__}.{self.model.id}",
            new_storage.all()
        )

    def test_reload_method(self):
        self.model.save()
        self.storage.reload()

        reloaded_model = self.storage.all().get(
            f"{self.model.__class__.__name__}.{self.model.id}"
        )
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(reloaded_model.id, self.model.id)

    def test_save_and_reload_multiple_models(self):
        models = [BaseModel() for _ in range(5)]
        for model in models:
            self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        for model in models:
            key = f"{model.__class__.__name__}.{model.id}"
            self.assertIn(key, new_storage.all())
            self.assertIsInstance(new_storage.all()[key], BaseModel)

    def test_reload_without_file(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_invalid_reload(self):
        # Remove the file before reloading
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

        # Reloading without a file should result in an empty __objects
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

        # Reloading again after deleting the file should not raise any error
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_invalid_reload_with_corrupted_file(self):
        # Create a corrupted file by writing an invalid JSON
        with open(FileStorage._FileStorage__file_path, 'w') as file:
            file.write("invalid json")

        # Reloading with a corrupted file should result in an empty __objects
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_new_method_with_existing_model(self):
        self.storage.new(self.model)
        initial_objects_count = len(self.storage.all())
        # Adding the same model again
        self.storage.new(self.model)
        updated_objects_count = len(self.storage.all())
        self.assertEqual(initial_objects_count, updated_objects_count)

    def test_save_method_with_existing_model(self):
        self.storage.new(self.model)
        initial_objects_count = len(self.storage.all())
        # Saving the same model again
        self.storage.save()
        updated_objects_count = len(self.storage.all())
        self.assertEqual(initial_objects_count, updated_objects_count)

    def test_all_method(self):
        models = [BaseModel() for _ in range(5)]
        for model in models:
            self.storage.new(model)
        all_models = self.storage.all()
        self.assertIsInstance(all_models, dict)
        for model in models:
            key = f"{model.__class__.__name__}.{model.id}"
            self.assertIn(key, all_models)
            self.assertIs(all_models[key], model)


if __name__ == '__main__':
    unittest.main()
