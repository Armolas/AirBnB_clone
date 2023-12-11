#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.state import State


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    state_model = State()

    def setUp(self):
        """set up method for instance info"""
        self.state_model.name = "Lagos"

    def test_user_info(self):
        """tests the information of user"""
        name = self.state_model.name
        self.assertEqual(name, "Lagos")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.state_model.name, str)