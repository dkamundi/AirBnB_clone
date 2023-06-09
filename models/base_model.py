#!/usr/bin/env python3
"""base class model to be inherited by other classes"""

from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        #self.id = str(uuid.uuid4())
        #self.created_at = datetime.now()
        #self.updated_at = datetime.now()
        # create a new instance
        #models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
                    #setattr(self, key, value)     
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel object."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel object."""
        dict_rep = dict(self.__dict__)
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        dict_rep["updated_at"] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        return (dict_rep)
