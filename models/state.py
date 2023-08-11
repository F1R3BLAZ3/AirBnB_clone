#!/usr/bin/python3

"""
This module defines the State class, which inherits from the BaseModel class.
It represents state objects and extends the common attributes and methods
provided by BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state object.

    This class inherits from the BaseModel class and adds attributes specific
    to state objects.

    Attributes:
        name (str): The name of the state.
    """

    # Initialize the 'name' attribute as a class variable
    name = ""
