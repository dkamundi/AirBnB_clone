#!/usr/bin/env python3
"""
initialize package
"""

from models.base_model import BaseModel as base
from models.engine.file_storage import FileStorage
from models.user import User


my_classes = {
        "BaseModel":base,
        "User": User
        }

storage = FileStorage()
storage.reload()
