#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    review_model = Review()

    def setUp(self):
        """set up method for instance info"""
        self.review_model.place_id = "12-34-e78"
        self.review_model.user_id = "12345"
        self.review_model.text = "A new review text"

    def test_user_info(self):
        """tests the information of user"""
        place_id = self.review_model.place_id
        user_id = self.review_model.user_id
        text = self.review_model.text
        self.assertEqual(place_id, "12-34-e78")
        self.assertEqual(user_id, "12345")
        self.assertEqual(text, "A new review text")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.review_model.place_id, str)
        self.assertIsInstance(self.review_model.user_id, str)
        self.assertIsInstance(self.review_model.text, str)

    def test_base_model_instance(self):
        """Tests if City inherits from BaseModel."""
        self.assertIsInstance(self.review_model, BaseModel)

    def test_attributes_exist(self):
        """Tests that attributes exist"""
        self.assertEqual(hasattr(self.review_model, "place_id"), True)
        self.assertEqual(hasattr(self.review_model, "user_id"), True)
        self.assertEqual(hasattr(self.review_model, "text"), True)
