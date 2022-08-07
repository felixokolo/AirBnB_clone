#!/usr/bin/python3
"""Base model package"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """City class
    Attributes:
        state_id (str): Associated state id
        name (str): City name
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
