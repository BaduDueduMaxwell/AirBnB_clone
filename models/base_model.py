#!/usr/bin/python3
"""This script is the base model"""

import uuid
import datetime
from models.base_model import BaseModel

class BaseModel:
    """defines all common attributes/methods for the other classes"""
    def __init__(self):
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