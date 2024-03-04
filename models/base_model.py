#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """__init__ method"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key is not "__class__":
                    setattr(self, key, value)
                if key is 'id':
                    self.id = value
                if key is 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key is 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()  
    
    def __str__(self):
        """__str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """save method"""
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """to_dict method"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['id'] = self.id
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
