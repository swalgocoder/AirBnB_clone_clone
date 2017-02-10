#!/usr/bin/python3
from models.base_model import BaseModel
"""
The Amenity module.
"""


class Amenity(BaseModel):
    """
    one public attribute, 'name'.
    """
    def __init__(self, *args, **kwargs):
        if type(args[0]) is dict:
            super().__init__(args[0])
        else:
            super().__init__()

        self.name = ''
