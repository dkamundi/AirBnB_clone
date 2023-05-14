#!/usr/bin/python3
"""Module for testing BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Create a new instance of BaseModel."""
        self.base = BaseModel()

    def test_init(self):
        """Test instance attributes of BaseModel."""
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """Test __str__ method of BaseModel."""
        expected = "[{}] ({}) {}".format(
            type(self.base).__name__, self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected)

    def test_save(self):
        """Test save method of BaseModel."""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel."""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertEqual(base_dict['__class__'], type(self.base).__name__)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_to_dict_with_different_format(self):
        """Test to_dict method of BaseModel with different format."""
        base_dict = self.base.to_dict("%Y%m%d%H%M%S%f")
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertEqual(base_dict['__class__'], type(self.base).__name__)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

