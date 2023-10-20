#!/usr/bin/python3
""" our basemodel function. """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        a basemodel class that takes care of the initialization,
        serialization and deserialization of instances in the program
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """instance initialization of basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], self.date_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], self.date_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            the string implementation of the basemodel
        """
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

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
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
