"""
Unit tests for the portion of this project which processes raw text using
natural language processing techniques.
"""

import unittest

# Magically manipulate sys.path
from testassets import pathmagic

from SocialNPHS.language import tweet
from SocialNPHS.sources.twitter import user


class testTweetLanguage(unittest.TestCase):
    def setUp(self):
        self.sentence = ("@1Defenestrator is really awesome! Although, "
                         "@G4_Y5_3X is cooler.")

    def test_tweet_tagging(self):
        # Test that tagging works in its most basic form
        moshe = user.NPUser("G4_Y5_3X")
        tags = tweet.get_tweet_tags(moshe.tweepy.status.text)
        self.assertIsInstance(tags, list)
        # Test that names are replaced and recognized as proper nouns
        tags = tweet.get_tweet_tags(self.sentence)
        self.assertEqual(tags[0][0], "Luke Taylor")
        self.assertEqual(tags[0][1], "NNP")

    def test_tweet_sentiment(self):
        # Test that basic sentiment analysis works
        self.assertEqual(
            tweet.tweet_connotation(self.sentence)['compound'],
            0.345
        )
        self.assertEqual(
            tweet.person_connotation(self.sentence, 'Luke Taylor')['neu'],
            0.461
        )
