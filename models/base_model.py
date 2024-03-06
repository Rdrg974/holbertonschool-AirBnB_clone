#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """__init__ method"""
        if kwargs:
            format_style = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format_style)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format_style)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """__str__ method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """to_dict method"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
