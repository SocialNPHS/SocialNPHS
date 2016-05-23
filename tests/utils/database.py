""" Tests of JSON read/write class """

import os
import sys
sys.path.insert(0, ".")

from SocialNPHS.utils.database import Database


# Path to test JSON file
path = os.path.abspath("tests/utils/testdb.json")


# -- Test changing the database, then restore -- #

# Create magical database class
db = Database(path)
# Store old value
old = db["cats"]
# Change value.
db["cats"] = "database corruption wreaks havoc upon this earth"
# Test that the file was changed by making a new instance and reading
stored = Database(path)["cats"]
assert stored == "database corruption wreaks havoc upon this earth"
# Restore
db["cats"] = old


# -- Test adding and deleting an item from the database, as well as db.get and
#    the semantic "in" -- #
db = Database(path)
db["penguins"] = "woah it's a penguin"
assert Database(path)["penguins"] == "woah it's a penguin"  # Make a new one
assert "penguins" in Database(path)
db.pop("penguins")
assert Database(path).get("penguins", "nope") == "nope"
assert "penguins" not in Database(path)
