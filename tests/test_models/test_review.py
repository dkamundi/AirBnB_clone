#!/usr/bin/env python3
"""unit test for review"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
