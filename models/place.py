#!usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    '''Place class that inherits from BaseModel'''
    """
    This is the place class

    Attributes:
        city_id (str): The city id
        user_id (str): The user id
        name (str): The name of the place/house
        description (str): The description of the place/house
        number_rooms (int): The number of rooms in the place/house
        number_bathrooms (int): The number of bathrooms in the place/house
        max_guest (int): The max number of guests the place/house can hold
        price_by_night (int): The price per night for the place/house
        latitude (float): The latitude of the place/house
        longitude (float): The longitude of the place/house
        amenity_ids (list): A list of amenity(ids) in the place/house
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
