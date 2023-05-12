#!/usr/bin/python3
"""FileStorage class that serializes
    instances to a JSON file and deserializes JSON file to instances
"""


import json


class FileStorage(object):
    """FileStorage class that serializes
    instances to a JSON file and deserializes JSON file to instances
    """
    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"

    # dictionary - empty but will store all objects by <class name>.id
    #   (ex: to store a BaseModel object with id=12121212,
    #       the key will be BaseModel.12121212)
    __objects = {}

    # ======= Instance Methods ===============
    def all(self):
        return type(self).__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__, obj.id)
        type(self).__objects[]

    def save(self):
        path = type(self).__file_path
        data = type(self).__objects

        with open(path, 'w') as fp:
            json.dump(data, fp)

    def reload(self):
        path = type(self).__file_path

        try:
            with open(path, 'r') as fp:
                type(self).__objects = json.load(data, fp)
        except FileNotFoundError:
            pass
