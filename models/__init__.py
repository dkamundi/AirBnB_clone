#!/usr/bin/env python3
"""
initialize package
"""

from models.base_model import BaseModel as base
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Reviews
from models.state import State


my_classes = {
        "BaseModel": base, "Place": Place,
        "User": User, "City": City,
        "State": State, "Reviews": Reviews,
        "Amenity": Amenity
        }

storage = FileStorage()
storage.reload()
