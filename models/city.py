#!/usr/bin/python3
'''city module'''


from models.base_model import BaseModel


class City(BaseModel):
    '''Defines a city and inherits from BaseModel'''

    state_id = ''
    name = ''
