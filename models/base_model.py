#!/usr/bin/python3
"""This script is the base model"""

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A method to convert the instance attributes to a dictionary format.
        Returns the dictionary representation of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
