#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    user_model = User()

    def setUp(self):
        """set up method for instance info"""
        self.user_model.email = "email@mail.com"
        self.user_model.first_name = "Foo"
        self.user_model.last_name = "Bar"
        self.user_model.password = "12345"

    def test_user_info(self):
        """tests the information of user"""
        email = self.user_model.email
        first_name = self.user_model.first_name
        last_name = self.user_model.last_name
        password = self.user_model.password
        self.assertEqual(email, "email@mail.com")
        self.assertEqual(first_name, "Foo")
        self.assertEqual(last_name, "Bar")
        self.assertEqual(password, "12345")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.user_model.first_name, str)
        self.assertIsInstance(self.user_model.last_name, str)
        self.assertIsInstance(self.user_model.email, str)
        self.assertIsInstance(self.user_model.password, str)

    def test_base_model_instance(self):
        """Tests if City inherits from BaseModel."""
        self.assertIsInstance(self.user_model, BaseModel)

    def test_attributes_exist(self):
        """Tests that attributes exist"""
        self.assertEqual(hasattr(self.user_model, "first_name"), True)
        self.assertEqual(hasattr(self.user_model, "last_name"), True)
        self.assertEqual(hasattr(self.user_model, "email"), True)
        self.assertEqual(hasattr(self.user_model, "password"), True)
