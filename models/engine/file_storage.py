#!/usr/bin/python3
"""
module that defines FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        This method returns the dictionary
        __object
        """
        return self.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj
        with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the
        JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f, indent=4)

    def reload(self):
        """
        This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            for key, value in data.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
