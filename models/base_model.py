#!/usr/bin/env python3
""" our basemodel function. """

import uuid
from datetime import datetime
import models
from models.engine import file_storage


class BaseModel:
    """
        a basemodel class that takes care of the initialization,
        serialization and deserialization of instances in the program
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """instance initialization of basemodel"""
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            date_keys = ["created_at", "updated_at"]
            for key in date_keys:
                kwargs[key] = datetime.strptime(kwargs[key], self.date_format)

            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
            the string implementation of the basemodel
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def __repr__(self):
        """
            this will return the string implementation
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            this one will update the datetime and save the object to a DB
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            this will return the converted object to dictionary representation
        """
        obj_to_dict = dict(self.__dict__)
        obj_to_dict['__class__'] = self.__class__.__name__
        obj_to_dict['created_at'] = self.updated_at.strftime(self.date_format)
        obj_to_dict['updated_at'] = self.created_at.strftime(self.date_format)

        return (obj_to_dict)
