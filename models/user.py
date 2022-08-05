#!/usr/bin/python3
"""Base model package"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """User class
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str) : User first name
        last_name (str) : User last name
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
