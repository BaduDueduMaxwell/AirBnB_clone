#!/usr/bin/python3
import json


class FileStorage:
    __file_path = 'file_json'
    __objects = {}

    def all(self):
        """
        Returns:
            dict: Returns the dictionary of all objects stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path)
        """
        with open(self.__file_path, 'w') as file:
            json.dump(k: v.to_dict() for k, v in self.__objects.items()), \
                file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
