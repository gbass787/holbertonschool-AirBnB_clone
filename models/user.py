#!/usr/bin/python3
"""
Defines User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User subclass of BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
