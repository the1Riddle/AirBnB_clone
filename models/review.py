#!/usr/bin/env python3
""" review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review model"""
    place_id = ""
    user_id = ""
    text = ""
