#!/usr/bin/python3
"""
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    ''' Private class attribute '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return type(self).__objects

    def new(self, obj):
        """Adds a new object to the dictionary."""
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())

        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """desirialises the json file to object if it exists"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
