#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User


classes = {
    'BaseModel': BaseModel,
    'User': User
}

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns:
            dict: Returns the dictionary of all objects stored.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

def reload(self):
        """Deserializes the JSON file to __objects (if exists)"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                for obj_data in obj_dict.values():
                    class_name = obj_data["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**obj_data)
                        self.new(obj)
