#!/usr/bin/python3
"""Base model package"""
from models.base_model import BaseModel
import models


class Amenity (BaseModel):
    """Amenity  class
    Attributes:
        name (str): Amenity  name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
