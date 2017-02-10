#!/usr/bin/python3
from models.base_model import BaseModel
"""
the State module.
"""


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        """
        the initialization function.
        """
        if type(args[0]) is dict:
            super().__init__(args[0])
        else:
            super().__init__()

        self.name = ''
