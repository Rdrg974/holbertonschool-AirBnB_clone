#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes the User"""
        super().__init__(*args, **kwargs)
