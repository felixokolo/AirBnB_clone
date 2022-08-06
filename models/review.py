#!/usr/bin/python3
"""Base model package"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Review  class
    Attributes:
        place_id (str): reviewed place id
        user_id (str): reviewer user id
        text (str): review description
    """
    
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
