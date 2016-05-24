"""
Unit tests for the portion of this project which collects text from social
media sources
"""

import sys
import unittest

from os import path

# PATH MAGIC
# Project root
base = path.abspath(path.join(path.dirname(path.abspath(__file__)), ".."))
sys.path.insert(0, base)

from SocialNPHS.sources.twitter import user
from SocialNPHS.sources.twitter import tweets


class testTwitter(unittest.TestCase):
    """ Test everything in SocialNPHS.sources.twitter """

    # user.py

    def test_basics(self):
        luke = user.NPUser("1Defenestrator")
        self.assertIsInstance(luke.followers, list)
        self.assertIsInstance(luke.following, list)
        self.assertIn(luke.grade, ["Freshman",
                                   "Sophomore",
                                   "Junior",
                                   "Senior"])
        self.assertIsInstance(luke.has_graduated, bool)

    def test_magicmethod(self):
        chris = user.NPUser("bravoc9")
        self.assertEqual(chris.fullname, "Chris Bravo")
        self.assertEqual(chris.sex, "M")

    def test_has_graduated(self):
        """ Test has_graduated by manipulating values """
        moshe = user.NPUser("G4_Y5_3X")
        moshe.user_info["grade"] = "3000"  # In the past
        self.assertFalse(moshe.has_graduated)
        moshe.user_info["grade"] = "2000"  # In the future
        self.assertTrue(moshe.has_graduated)
        moshe.user_info["grade"] = "2017"  # Reset

    # tweets.py

    def test_list(self):
        t = tweets.get_nphs_tweets()
        self.assertIsInstance(t, list)
        self.assertIsInstance(t[0], str)
