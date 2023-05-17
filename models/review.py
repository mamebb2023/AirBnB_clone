#!/usr/bin/env python3
""" Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the class Review """

    place_id = ""
    user_id = ""
    text = ""