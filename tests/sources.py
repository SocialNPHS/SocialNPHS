"""
Unit tests for the portion of this project which collects text from social
media sources
"""

import unittest

# Magically manipulate sys.path
from testassets import pathmagic

from SocialNPHS.sources.twitter import user
from SocialNPHS.sources.twitter import tweets


# TWITTER TESTS

class TestUser(unittest.TestCase):
    """ Test SocialNPHS.sources.twitter.user """

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

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            user.NPUser("this_is_too_long_to_be_a_twitter_handle")


class testTweets(unittest.TestCase):
    """ Test SocialNPHS.sources.twitter.tweets """
    def test_list(self):
        t = tweets.get_nphs_tweets()
        self.assertIsInstance(t, list)
        self.assertIsInstance(t[0], str)


class testDiscovery(unittest.TestCase):
    """ Test SocialNPHS.sources.twitter.discover """
    pass


# INSTAGRAM TESTS

class TestNotImplemented(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(NotImplementedError):
            import SocialNPHS.sources.instagram
