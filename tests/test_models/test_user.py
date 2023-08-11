import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_user_inherits_from_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_has_email_attribute(self):
        self.assertTrue(hasattr(User, 'email'))
        self.assertEqual(User.email, "")

    def test_user_has_password_attribute(self):
        self.assertTrue(hasattr(User, 'password'))
        self.assertEqual(User.password, "")

    def test_user_has_first_name_attribute(self):
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertEqual(User.first_name, "")

    def test_user_has_last_name_attribute(self):
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertEqual(User.last_name, "")

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_str_representation(self):
        user = User()
        str_rep = str(user)
        self.assertIn("[User]", str_rep)
        self.assertIn(user.id, str_rep)
        self.assertIn(str(user.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
