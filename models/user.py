#!/usr/bin/env python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new User"""
        super().__init__(*args, **kwargs)
