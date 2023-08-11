import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_review_inherits_from_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_has_place_id_attribute(self):
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertEqual(Review.place_id, "")

    def test_review_has_user_id_attribute(self):
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertEqual(Review.user_id, "")

    def test_review_has_text_attribute(self):
        self.assertTrue(hasattr(Review, 'text'))
        self.assertEqual(Review.text, "")

    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_str_representation(self):
        review = Review()
        str_rep = str(review)
        self.assertIn("[Review]", str_rep)
        self.assertIn(review.id, str_rep)
        self.assertIn(str(review.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
