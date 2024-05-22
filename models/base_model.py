#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is not empty:
            - Each key-value pair in kwargs represents an attribute name \
              and its value.
            - id and created_at are created as in the previous \
              implementation.
        Otherwise:
            - id and created_at are generated as in the previous \
              implementation.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(\
                                                             value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    def __str__(self):
        """
        Returns a string representation of the BaseModel object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, \
                                     self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object.
        Converts created_at and updated_at to ISO format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value), value))
