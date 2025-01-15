"""User model class"""
#!usr/bin/python3
from models.base_model import BaseModel

'''User class'''
class User(BaseModel):
    '''User class that inherits from BaseModel'''
    pass
    """
    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.
        """
        super().__init__(*args, **kwargs)

        # self.email = User.email
        # self.password = User.password
        # self.first_name = User.first_name
        # self.last_name = User.last_name
