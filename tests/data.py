"""
Unit tests for the portion of this project which collects text from social
media sources
"""

import unittest

import livejson
import shapefile

# Magically manipulate sys.path
from testassets import pathmagic

import SocialNPHS.data
from SocialNPHS.data import twitter_users
from SocialNPHS.data import district_bounds


class TestDistrictData(unittest.TestCase):
    data = district_bounds.ShapeFileData()

    def test_loading(self):
        """ Test loading the data into memory """
        self.assertIsInstance(self.data.districts, list)

    def test_retrieval(self):
        """ Test that we can retrieve actual data """
        self.assertIsInstance(self.data.get_district_by_name(
            "New Paltz Central School District"
        ), shapefile._ShapeRecord)
        self.assertIsInstance(SocialNPHS.data.district, shapefile._ShapeRecord)

        with self.assertRaises(IndexError):
            self.data.get_district_by_name(
                "Nobody would name a school district with such a name!"
            )


class TestTwitterUsers(unittest.TestCase):
    def test_basic(self):
        self.assertIsInstance(twitter_users.students, livejson.DictDatabase)
