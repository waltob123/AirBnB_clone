#!/usr/bin/python3
'''user module'''


from models.base_model import BaseModel


class User(BaseModel):
    '''A class that defines a user and inherits
    from the BaseModel

    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): firstname of the user
        last_name (str): lastname of the user
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
