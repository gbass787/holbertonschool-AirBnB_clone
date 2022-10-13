#!/usr/bin/python3
"""Defines a city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city. inherits from BaseModel
    """
    state_id = ""
    name = ""
