#!/usr/bin/python3
"""test BaseModel module"""
import datetime
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class for the BaseModel"""

    model = BaseModel()

    def test_unique_id(self):
        """tests for unique ids"""
        u_ids = set()
        for _id in range(200):
            u_id_model = BaseModel()
            self.assertNotIn(u_id_model.id, u_ids)
            u_ids.add(u_id_model.id)

    def test_id_str(self):
        """tests the type of id"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """tests for creation date type"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at(self):
        """tests for update date type"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_str(self):
        """test for string method"""
        output = (
            f"[{self.model.__class__.__name__}]"
            f" ({self.model.id}) {self.model.__dict__}"
        )
        self.assertEqual(str(self.model), output)

    def test_save(self):
        """test for save method"""
        older_date = self.model.updated_at
        self.model.save()
        self.assertLess(older_date, self.model.updated_at)

    def test_to_dict(self):
        """test for to_dict method"""
        model_dict = self.model.to_dict()
        expected_dict = dict(self.model.__dict__)
        expected_dict["created_at"] = self.model.created_at.isoformat()
        expected_dict["updated_at"] = self.model.updated_at.isoformat()
        expected_dict["__class__"] = self.model.__class__.__name__
        self.assertEqual(model_dict, expected_dict)

    def test_to_dict_type(self):
        """tests for the type returned by to_dict method"""
        expected_dict = dict(self.model.__dict__)
        expected_dict["created_at"] = self.model.created_at.isoformat()
        expected_dict["updated_at"] = self.model.updated_at.isoformat()
        expected_dict["__class__"] = self.model.__class__.__name__
        self.assertIsInstance(expected_dict, dict)

    def test_to_dict_new_attrs(self):
        """Tests for attributes in instance after call to to_dict()"""
        self.model.name = "NewName"
        self.model.model_number = 20

        new_dict = dict(self.model.__dict__)
        new_dict["__class__"] = self.model.__class__.__name__
        new_dict["created_at"] = self.model.created_at.isoformat()
        new_dict["updated_at"] = self.model.updated_at.isoformat()

        self.assertIn("name", self.model.to_dict())
        self.assertIn("model_number", self.model.to_dict())
        self.assertEqual(new_dict, self.model.to_dict())

    def test_attributes_exist(self):
        """Tests that attributes exist"""
        self.assertEqual(hasattr(self.model, "id"), True)
        self.assertEqual(hasattr(self.model, "created_at"), True)
        self.assertEqual(hasattr(self.model, "updated_at"), True)
