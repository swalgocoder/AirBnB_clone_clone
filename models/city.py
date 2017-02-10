#!/usr/bin/python3
from models.base_model import BaseModel
"""
The City module.
"""


class City(BaseModel):
    """
    two public attributes: 'state_id' and 'name'x
    """
    def __init__(self, *args, **kwargs):
        if type(args[0]) is dict:
            super().__init__(args[0])
        else:
            super().__init__()

        self.state_id = ''
        self.name = ''
