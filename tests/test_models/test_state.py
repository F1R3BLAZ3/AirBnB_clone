import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_state_inherits_from_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_has_name_attribute(self):
        self.assertTrue(hasattr(State, 'name'))
        self.assertEqual(State.name, "")

    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_str_representation(self):
        state = State()
        str_rep = str(state)
        self.assertIn("[State]", str_rep)
        self.assertIn(state.id, str_rep)
        self.assertIn(str(state.__dict__), str_rep)


if __name__ == '__main__':
    unittest.main()
