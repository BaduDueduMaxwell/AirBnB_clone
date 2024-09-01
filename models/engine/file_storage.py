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
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                    for obj_data in obj_dict.values():
                        class_name = obj_data.get("__class__")
                        cls = classes.get(class_name)
                        if cls:
                            obj = cls(**obj_data)
                            self.new(obj)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading or parsing file: {e}")
