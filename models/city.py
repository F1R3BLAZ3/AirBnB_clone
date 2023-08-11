#!/usr/bin/python3

"""
This module defines the City class, which inherits from the BaseModel class.
It represents city objects and extends the common attributes and methods
provided by BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city object.

    This class inherits from the BaseModel class and adds attributes specific
    to city objects.

    Attributes:
        state_id (str): The ID of the state where the city is located.
        name (str): The name of the city.
    """

    # Initialize the attributes as class variables
    state_id = ""
    name = ""
