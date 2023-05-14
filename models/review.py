#!/usr/bin/env python3
"""module for review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class"""
    place_id = ""
    user_id = ""
    text = ""
