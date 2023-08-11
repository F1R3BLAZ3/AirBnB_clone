import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def test_city_inherits_from_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_has_state_id_attribute(self):
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertEqual(City.state_id, "")

    def test_city_has_name_attribute(self):
        self.assertTrue(hasattr(City, 'name'))
        self.assertEqual(City.name, "")

    def test_city_state_id_is_string(self):
        self.assertIsInstance(City.state_id, str)

    def test_city_name_is_string(self):
        self.assertIsInstance(City.name, str)

    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_str_representation(self):
        city = City()
        str_rep = str(city)
        self.assertIn("[City]", str_rep)
        self.assertIn(city.id, str_rep)
        self.assertIn(str(city.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
