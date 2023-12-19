#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    place_model = Place()

    def setUp(self):
        """set up method for instance info"""
        self.place_model.city_id = "12-34-567"
        self.place_model.user_id = "12345"
        self.place_model.name = "Name"
        self.place_model.description = "description of place"
        self.place_model.number_rooms = 25
        self.place_model.number_bathrooms = 2
        self.place_model.max_guest = 4
        self.place_model.price_by_night = 500
        self.place_model.longitude = 15.87
        self.place_model.latitude = 12.23
        self.place_model.amenity_ids = ["123", "456", "789"]

    def test_user_info(self):
        """tests the information of user"""
        city_id = self.place_model.city_id
        user_id = self.place_model.user_id
        name = self.place_model.name
        description = self.place_model.description
        number_rooms = self.place_model.number_rooms
        number_bathrooms = self.place_model.number_bathrooms
        max_guest = self.place_model.max_guest
        price_by_night = self.place_model.price_by_night
        longitude = self.place_model.longitude
        latitude = self.place_model.latitude
        amenity_ids = self.place_model.amenity_ids
        self.assertEqual(city_id, "12-34-567")
        self.assertEqual(user_id, "12345")
        self.assertEqual(name, "Name")
        self.assertEqual(description, "description of place")
        self.assertEqual(number_rooms, 25)
        self.assertEqual(number_bathrooms, 2)
        self.assertEqual(max_guest, 4)
        self.assertEqual(price_by_night, 500)
        self.assertEqual(longitude, 15.87)
        self.assertEqual(latitude, 12.23)
        self.assertEqual(amenity_ids, ["123", "456", "789"])

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.place_model.city_id, str)
        self.assertIsInstance(self.place_model.user_id, str)
        self.assertIsInstance(self.place_model.name, str)
        self.assertIsInstance(self.place_model.description, str)
        self.assertIsInstance(self.place_model.number_rooms, int)
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertIsInstance(self.place_model.max_guest, int)
        self.assertIsInstance(self.place_model.price_by_night, int)
        self.assertIsInstance(self.place_model.longitude, float)
        self.assertIsInstance(self.place_model.latitude, float)
        self.assertIsInstance(self.place_model.amenity_ids, list)

    def test_base_model_instance(self):
        """Tests if City inherits from BaseModel."""
        self.assertIsInstance(self.place_model, BaseModel)

    def test_attributes_exist(self):
        """Tests that attributes exist"""
        self.assertEqual(hasattr(self.place_model, "city_id"), True)
        self.assertEqual(hasattr(self.place_model, "user_id"), True)
        self.assertEqual(hasattr(self.place_model, "name"), True)
        self.assertEqual(hasattr(self.place_model, "description"), True)
        self.assertEqual(hasattr(self.place_model, "number_rooms"), True)
        self.assertEqual(hasattr(self.place_model, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.place_model, "max_guest"), True)
        self.assertEqual(hasattr(self.place_model, "price_by_night"), True)
        self.assertEqual(hasattr(self.place_model, "longitude"), True)
        self.assertEqual(hasattr(self.place_model, "latitude"), True)
        self.assertEqual(hasattr(self.place_model, "amenity_ids"), True)
