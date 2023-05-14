#!/usr/bin/env python3
"""file storage module"""

import json
import models
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class namee>.id."""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        val = obj
        FileStorage.__objects[key] = val

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)
                for k, v in objs.items():
                    class_name = v['__class__']
                    if class_name == 'BaseModel':
                        obj = BaseModel(**v)
                    elif class_name == 'User':
                        obj = User(**v)
                    else:
                        continue
                    FileStorage.__objects[k] = obj
