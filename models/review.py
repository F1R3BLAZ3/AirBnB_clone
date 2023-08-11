#!/usr/bin/python3

"""
This module defines the Review class, which inherits from the BaseModel class.
It represents review objects and extends the common attributes and methods
provided by BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review object.

    This class inherits from the BaseModel class and adds attributes specific
    to review objects.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    # Initialize the attributes as class variables
    place_id = ""
    user_id = ""
    text = ""
