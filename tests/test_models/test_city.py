#!/usr/bin/env python3
"""unittest for city"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

