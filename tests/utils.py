"""
Unit tests for the portion of this project which provides utilities to be used
by other parts of this project.
"""

import sys
import unittest

from os import path

# PATH MAGIC
# Project root
base = path.abspath(path.join(path.dirname(path.abspath(__file__)), ".."))
sys.path.insert(0, base)

from SocialNPHS.utils.database import Database


# Path to JSON file
dbpath = path.join(base, "tests/testassets/testdb.json")


class testTwitter(unittest.TestCase):
    def test_basic_usage(self):
        db = Database(dbpath)
        old = db["cats"]  # Store old value

        # Change value
        msg = "database corruption wreaks havoc upon this earth"
        db["cats"] = msg
        # Test that the file was changed by making a new instance and reading
        stored = Database(dbpath)["cats"]
        self.assertEqual(stored, msg)
        # Restore
        db["cats"] = old

    def test_fancy_stuff(self):
        """ Test adding and deleting an item from the database, as well as
        db.get and the semantic "in" """

        db = Database(dbpath)
        db["penguins"] = "woah it's a penguin"
        self.assertEqual(Database(dbpath)["penguins"], "woah it's a penguin")
        self.assertIn("penguins", Database(dbpath))     # test semantic in
        db.pop("penguins")                              # test pop
        self.assertEqual(Database(dbpath).get("penguins", "nope"), "nope")
        self.assertNotIn("penguins", Database(dbpath))  # test reverse
