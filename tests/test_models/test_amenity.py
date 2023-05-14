#!/usr/bin/env python3
"""unittests for amendity"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
