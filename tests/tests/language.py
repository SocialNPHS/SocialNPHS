"""
Unit tests for the portion of this project which processes raw text using
natural language processing techniques.
"""

import sys
import unittest

from os import path

# PATH MAGIC
# Project root
base = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../.."))
sys.path.insert(0, base)

from SocialNPHS.language import tweet
from SocialNPHS.sources.twitter import user


class testLanguage(unittest.TestCase):
    def test_tweet(self):
        moshe = user.NPUser("G4_Y5_3X")
        tags = tweet.get_tweet_tags(moshe.User.status.text)
        self.assertIsInstance(tags, list)
