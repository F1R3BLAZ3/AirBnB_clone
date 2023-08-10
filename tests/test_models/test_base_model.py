#!/usr/bin/python3
import unittest
import datetime
import os
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_str_method(self):
        self.assertEqual(
            str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}")

    def test_save_method_updates_updated_at(self):
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_new_instance_creates_new_entry_in_storage(self):
        storage_count_before = len(storage.all())
        new_model = BaseModel()
        storage_count_after = len(storage.all())
        self.assertEqual(storage_count_after, storage_count_before + 1)

    def test_kwargs_constructor(self):
        kwargs = {'id': 'test_id',
                  'created_at': '2023-08-10T12:00:00.000000', 'name': 'Test'}
        model_with_kwargs = BaseModel(**kwargs)
        self.assertEqual(model_with_kwargs.id, 'test_id')
        self.assertEqual(model_with_kwargs.name, 'Test')
        self.assertIsInstance(model_with_kwargs.created_at, datetime.datetime)

    def test_new_instance_has_id_created_updated_attributes(self):
        new_model = BaseModel()
        self.assertTrue(hasattr(new_model, 'id'))
        self.assertTrue(hasattr(new_model, 'created_at'))
        self.assertTrue(hasattr(new_model, 'updated_at'))

    def test_new_instance_with_id_kwarg(self):
        kwargs_with_id = {'id': 'test_id'}
        model_with_id = BaseModel(**kwargs_with_id)
        self.assertEqual(model_with_id.id, 'test_id')

    def test_new_instance_with_created_at_kwarg(self):
        created_at_string = '2023-08-10T12:00:00.000000'
        kwargs_with_created_at = {'created_at': created_at_string}
        model_with_created_at = BaseModel(**kwargs_with_created_at)
        expected_created_at = datetime.datetime.strptime(
            created_at_string, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(model_with_created_at.created_at, expected_created_at)

    def test_new_instance_without_args_or_kwargs(self):
        new_model = BaseModel()
        self.assertIsNotNone(new_model.id)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)

    def test_save_method_updates_storage(self):
        storage_count_before = len(storage.all())
        new_model = BaseModel()
        new_model.save()
        storage_count_after = len(storage.all())
        self.assertEqual(storage_count_after, storage_count_before + 1)

    def test_reload_method(self):
        new_model = BaseModel()
        new_model.save()
        storage.save()
        storage.reload()
        reloaded_model = storage.all().get(
            f"{BaseModel.__name__}.{new_model.id}")
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(reloaded_model.id, new_model.id)

    def test_reload_method_without_file(self):
        # Remove the file before reloading
        file_path = storage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)

        storage.reload()

        # Check that __objects is an empty dictionary
        self.assertEqual(len(storage.all()), 0)

    def test_str_method_with_extra_attributes(self):
        # Add extra attributes to the instance
        self.model.extra_attr = "extra_value"
        self.model.another_attr = "another_value"
        str_output = str(self.model)
        self.assertIn("extra_attr", str_output)
        self.assertIn("another_attr", str_output)

    def test_invalid_updated_at_string(self):
        kwargs = {'updated_at': 'invalid_format'}
        with self.assertRaises(ValueError):
            BaseModel(**kwargs)


if __name__ == '__main__':
    unittest.main()
