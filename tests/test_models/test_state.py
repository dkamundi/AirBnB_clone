#!/usr/bin/env python3
"""unittests for class state"""

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")
