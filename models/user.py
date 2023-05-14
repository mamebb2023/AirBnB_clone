#!/usr/bin/env python3
""" User that inherits form BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""