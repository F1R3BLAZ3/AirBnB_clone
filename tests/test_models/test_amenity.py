import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_amenity_inherits_from_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_name_attribute(self):
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertEqual(Amenity.name, "")

    def test_amenity_name_is_string(self):
        self.assertIsInstance(Amenity.name, str)

    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_str_representation(self):
        amenity = Amenity()
        str_rep = str(amenity)
        self.assertIn("[Amenity]", str_rep)
        self.assertIn(amenity.id, str_rep)
        self.assertIn(str(amenity.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
