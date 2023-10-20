#!/usr/bin/env python3
""" Class user """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
