#!/usr/bin/python3

"""
This script initializes the FileStorage instance and reloads data from the
JSON file.

It creates an instance of the FileStorage class and loads the stored data
from the JSON file, populating the internal dictionary of objects.
"""

from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload data from the JSON file, populating the dictionary of objects
storage.reload()
