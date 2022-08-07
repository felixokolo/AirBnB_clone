#!/usr/bin/python3
"""Base model package"""
from models.base_model import BaseModel
import models


class Place  (BaseModel):
    """Amenity  class
    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): Place name
        description (str): place description
        number_rooms (int): number of rooms in place
        number_bathrooms (int): number of bathrooms in place
        max_guest (int): number of maximum guests in place
        price_by_night (int): price of place per night
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (list): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
