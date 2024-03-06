#!/usr/bin/python3
"""Module for Base Model unittests."""
import uuid
import unittest
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests Base Model class."""
    def test_save(self):
        """Test save()"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_save_updates_file(self):
        my_model = BaseModel()
        my_model.save()
        bmid = "BaseModel." + my_model.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_to_dict(self):
        """Test to_dict()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
<<<<<<< HEAD
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"],
                         my_model.created_at.isoformat())
=======
        id1 = my_model_json["id"]
        id2 = my_model.id
        created1 = my_model_json["created_at"]
        created2 = my_model.created_at.isoformat()
        self.assertNotEqual(id1, id2)
        self.assertEqual(created1, created2)
>>>>>>> 2816098 (test_base_model.py)

    def test__str__(self):
        """Test __str__()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
<<<<<<< HEAD
        self.assertEqual(str(my_model),
                         f"[BaseModel] ({my_model.id}) {my_model.__dict__}")
=======
        s1 = str(my_model)
        s2 = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(s1, s2)
>>>>>>> 2816098 (test_base_model.py)

    def test_init(self):
        """Test __init__()"""
        my_model = BaseModel()

        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)


    if __name__ == "__main__":
        unittest.main()
