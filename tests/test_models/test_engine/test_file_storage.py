#!/usr/bin/python3
"""Module for testing FileStorage class."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Create a new instance of FileStorage."""
        cls.file = "test_file.json"
        if os.path.exists(cls.file):
            os.remove(cls.file)
        cls.storage = FileStorage(cls.file)
        cls.storage.reload()

    def setUp(self):
        """Create a new instance of BaseModel."""
        self.base = BaseModel()
        self.base.save()

    def tearDown(self):
        """Delete the instance of BaseModel."""
        del self.base

    def test_all(self):
        """Test all method of FileStorage."""
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIn(type(self.base).__name__ + '.' + self.base.id, objs)

    def test_new(self):
        """Test new method of FileStorage."""
        base2 = BaseModel()
        self.storage.new(base2)
        objs = self.storage.all()
        self.assertIn(type(base2).__name__ + '.' + base2.id, objs)

    def test_save(self):
        """Test save method of FileStorage."""
        self.storage.save()
        with open(self.file, 'r') as f:
            text = f.read()
            self.assertIn(type(self.base).__name__ + '.' + self.base.id, text)

    def test_reload(self):
        """Test reload method of FileStorage."""
        with open(self.file, 'w') as f:
            f.write('{}')
        self.storage.reload()
        objs = self.storage.all()
        self.assertEqual(objs, {})


if __name__ == '__main__':
    unittest.main()

