#!usr/bin/env python3
from models.base_model import BaseModel

'''City class'''
class City(BaseModel):
    '''City class that inherits from BaseModel'''
      Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = City.name
        # self.state_id = City.state_id
