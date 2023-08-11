import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def test_place_inherits_from_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_has_city_id_attribute(self):
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertEqual(Place.city_id, "")

    def test_place_has_user_id_attribute(self):
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertEqual(Place.user_id, "")

    def test_place_has_name_attribute(self):
        self.assertTrue(hasattr(Place, 'name'))
        self.assertEqual(Place.name, "")

    def test_place_has_description_attribute(self):
        self.assertTrue(hasattr(Place, 'description'))
        self.assertEqual(Place.description, "")

    def test_place_has_number_rooms_attribute(self):
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertEqual(Place.number_rooms, 0)

    def test_place_has_number_bathrooms_attribute(self):
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertEqual(Place.number_bathrooms, 0)

    def test_place_has_max_guest_attribute(self):
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertEqual(Place.max_guest, 0)

    def test_place_has_price_by_night_attribute(self):
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertEqual(Place.price_by_night, 0)

    def test_place_has_latitude_attribute(self):
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertEqual(Place.latitude, 0.0)

    def test_place_has_longitude_attribute(self):
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertEqual(Place.longitude, 0.0)

    def test_place_has_amenity_ids_attribute(self):
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertEqual(Place.amenity_ids, [])

    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_place_str_representation(self):
        place = Place()
        str_rep = str(place)
        self.assertIn("[Place]", str_rep)
        self.assertIn(place.id, str_rep)
        self.assertIn(str(place.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
