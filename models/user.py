#!/usr/bin/python3

"""
This module defines the User class, which inherits from the BaseModel class.
It represents user objects and extends the common attributes and methods
provided by BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user object.

    This class inherits from the BaseModel class and adds attributes specific
    to user objects.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    # Initialize attributes as class variables
    email = ""
    password = ""
    first_name = ""
    last_name = ""
