#!/usr/bin/python3
"""Defines a review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review. inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
