"""
Unit tests for the portion of this project which processes raw text using
natural language processing techniques.
"""

import sys
import unittest

from os import path

# PATH MAGIC
# Project root
base = path.abspath(path.join(path.dirname(path.abspath(__file__)), ".."))
sys.path.insert(0, base)

from SocialNPHS.language import tweet
from SocialNPHS.sources.twitter import user


class testLanguage(unittest.TestCase):
    test = "@1Defenestrator is really awesome! Although, @G4_Y5_3X is cooler."

    def test_tweet_tagging(self):
        # Test that tagging works in its most basic form
        moshe = user.NPUser("G4_Y5_3X")
        tags = tweet.get_tweet_tags(moshe.tweepy.status.text)
        self.assertIsInstance(tags, list)
        # Test that names are replaced and recognized as proper nouns
        tags = tweet.get_tweet_tags(test)
        self.assertEqual(tags[0][0], "Luke Taylor")
        self.assertEqual(tags[0][1], "NNP")

    def test_tweet_analysis(self):
        # Test that basic sentiment analysis works (current values hardcoded)
        self.assertEqual(tweet.tweet_connotation(test)['compound'], 0.345)
        self.assertEqual(tweet.person_connotation(test, 'Luke Taylor')['neu'],
                         0.461)  # pep8 line limit bite my shiny python ass
