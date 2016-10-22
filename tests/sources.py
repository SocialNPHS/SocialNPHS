"""
Unit tests for the portion of this project which collects text from social
media sources
"""

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

# Magically manipulate sys.path
from testassets import pathmagic

from SocialNPHS.sources.twitter import discover
from SocialNPHS.sources.twitter import user
from SocialNPHS.sources.twitter import tweets
from SocialNPHS.sources.twitter.auth import api


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
        with self.assertRaises(AttributeError):
            chris.this_is_not_a_valid_attribute

    def test_has_graduated(self):
        """ Test has_graduated by manipulating values """
        moshe = user.NPUser("G4_Y5_3X")
        moshe.user_info["grade"] = "3000"  # In the past
        self.assertFalse(moshe.has_graduated)
        moshe.user_info["grade"] = "2000"  # In the future
        self.assertTrue(moshe.has_graduated)
        moshe.user_info["grade"] = "2017"  # Reset

    def test_misc(self):
        with self.assertRaises(ValueError):
            user.NPUser("this_is_too_long_to_be_a_twitter_handle")


class TestTweets(unittest.TestCase):
    """ Test SocialNPHS.sources.twitter.tweets """
    def test_list(self):
        t = tweets.get_nphs_tweets()
        self.assertIsInstance(t, list)
        self.assertIsInstance(t[0], str)


class TestDiscovery(unittest.TestCase):
    """ Test SocialNPHS.sources.twitter.discover """
    # Setting up mock Twitter users to do these tests consistently
    chris = MagicMock(
        id='c',
        location='New Paltz, NY',
        screen_name='bravoc9',
        followers_count=2
    )
    luke = MagicMock(
        id='l',
        location='New Paltz',
        screen_name='1Defenestrator',
        followers_count=4
    )
    moshe = MagicMock(
        id='m',
        location='New Paltz NY',
        screen_name='G4_Y5_3X',
        followers_count=2
    )
    michael = MagicMock(
        id='b',
        location='New Paltz',
        screen_name='iceberger',
        followers_count=0
    )
    rock = MagicMock(
        id='r',
        location='Da Qiu, China',
        screen_name='TheRock',
        followers_count=10390547
    )

    chris.followers = [luke, moshe]
    chris.following = [luke, rock]

    luke.followers = [chris, moshe, rock, michael]
    luke.following = [chris, moshe, rock]

    moshe.followers = [luke, rock]
    moshe.following = [chris, luke, rock]

    michael.followers = []
    michael.following = [luke]

    rock.followers = [chris, luke, moshe]
    rock.following = [luke, moshe]

    def test_association(self):
        users = discover.discover_by_association(self.luke, 3, 2)
        # Chris isn't famous and has enough people from NP following him
        self.assertTrue('bravoc9' in users)
        # Rock is too famous, Moshe only has 1 NP student following him
        self.assertFalse('G4_Y5_3X' in users)
        self.assertFalse('TheRock' in users)

    def test_location(self):
        users = discover.discover_by_location(self.luke, 6)
        self.assertTrue('G4_Y5_3X' in users)
        self.assertFalse('TheRock' in users)

    def test_geolocation(self):
        with patch('SocialNPHS.sources.twitter.auth.api') as mock_api:
            mock_tweets = {
                'c': [MagicMock(place=MagicMock(attributes={
                    'postal_code': '12561'}))],
                'l': [MagicMock(place=MagicMock(contained_within=[{
                    'name': 'New Paltz'}]))],
                'm': [MagicMock(place=MagicMock(contained_within=[{
                    'bounding_box': MagicMock(
                        coordinates=[[
                            (-74.205, 41.695), (-74.205, 41.711),
                            (-73.037, 41.711), (-73.037, 41.695)
                        ]])}]))],
                'b': [MagicMock(place=MagicMock(contained_within=[{
                    'name': 'New Paltz'}]))],
                'r': [MagicMock(place=None)]
            }

            def return_method(id):
                return mock_tweets[id]
            mock_api.user_timeline = MagicMock(side_effect=return_method)
            users = discover.discover_by_geolocation(self.luke, 6, _api=mock_api)
            self.assertTrue('G4_Y5_3X' in users)
            self.assertTrue('iceberger' in users)
            self.assertFalse('TheRock' in users)


# INSTAGRAM TESTS
class TestNotImplemented(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(NotImplementedError):
            import SocialNPHS.sources.instagram
