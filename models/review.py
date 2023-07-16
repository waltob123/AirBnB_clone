#!/usr/bin/python3
'''review module'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''Defines a review and inherits from BaseModel'''

    place_id = ''
    user_id = ''
    text = ''
