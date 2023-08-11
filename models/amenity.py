#!/usr/bin/python3

"""
This module contains the Amenity class, which represents amenities
that can be associated with other models.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for representing amenities.

    This class inherits from the BaseModel class and represents amenities
    that can be associated with other models.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""  # Default value for the 'name' attribute
