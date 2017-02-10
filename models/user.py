#!/usr/bin/python3
from models.base_model import BaseModel
"""
The User module.

User class subclassing and  inheriting from the BaseModel class.
"""



class User(BaseModel):
    def __init__(self):
        """
        initializing User with class attributes defaulting to empty strings.
        """
        super().__init__()

        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
