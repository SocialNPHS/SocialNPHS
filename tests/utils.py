"""
Unit tests for the portion of this project which provides utilities to be used
by other parts of this project.
"""

import os
import unittest

# Magically manipulate sys.path
from testassets import pathmagic

from SocialNPHS.utils.database import Database


class testDatabase(unittest.TestCase):
    """ Test the magical JSON database class """
    def setUp(self):
        # Path to JSON file
        self.dbpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "testassets/testdb.json")

    def test_basic_usage(self):
        db = Database(self.dbpath)
        old = db["cats"]  # Store old value

        # Change value
        msg = "database corruption wreaks havoc upon this earth"
        db["cats"] = msg
        # Test that the file was changed by making a new instance and reading
        stored = Database(self.dbpath)["cats"]
        self.assertEqual(stored, msg)
        # Restore
        db["cats"] = old

    def test_fancy_stuff(self):
        """ Test adding and deleting an item from the database, as well as
        db.get and the semantic "in" """

        db = Database(self.dbpath)
        db["penguins"] = "woah it's a penguin"
        self.assertEqual(Database(self.dbpath)["penguins"],
                         "woah it's a penguin")
        self.assertIn("penguins", Database(self.dbpath))
        db.pop("penguins")
        self.assertEqual(Database(self.dbpath).get("penguins", "nope"), "nope")
        self.assertNotIn("penguins", Database(self.dbpath))
