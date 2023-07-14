#!/usr/bin/python3
'''file_storage module'''


import json
import os


class FileStorage:
    '''
    Defines a class for serialization and deserialization
    of instances and JSON files respectively.

    Attributes:
        __file_path (str): Path to the file to save to
        __objects (dict): A dictionary containing instatiated objects
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Returns the public attribute __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key obj class name.id
        '''
        class_name = obj.__class__.__name__
        FileStorage.__objects[f'{class_name}.{obj.id}'] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        objs_dict = {obj: FileStorage.__objects[obj].to_dict() for obj in
                     FileStorage.__objects.keys()}
        with open(FileStorage.__objects, 'w') as json_file:
            json.dump(objs_dict, json_file)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                objs_dict = json.load(json_file)
                for dict_obj in objs_dict.values():
                    class_name = dict_obj['__class__']
                    self.new(eval(class_name)(**dict_obj))
        else:
            return
