#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    amenity_model = Amenity()

    def setUp(self):
        """set up method for instance info"""
        self.amenity_model.name = "Housing and Hospitality"

    def test_user_info(self):
        """tests the information of user"""
        name = self.amenity_model.name
        self.assertEqual(name, "Housing and Hospitality")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.amenity_model.name, str)

    def test_base_model_instance(self):
        """Tests if City inherits from BaseModel."""
        self.assertIsInstance(self.amenity_model, BaseModel)

    def test_attributes_exist(self):
        """Tests that attributes exist"""
        self.assertEqual(hasattr(self.amenity_model, "name"), True)
