#!/usr/bin/env python3
"""
initialize package
"""

from models.base_model import BaseModel as base
from models.engine.file_storage import FileStorage


my_classes = {
        "BaseModel":base
        }

storage = FileStorage()
storage.reload()
