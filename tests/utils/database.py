""" Tests of JSON read/write class """

import os
import sys
sys.path.insert(0, ".")

from SocialNPHS.utils.database import Database

# -- Test changing the database, then restore -- #
path = os.path.abspath("tests/utils/testdb.json")
# Create magical database class
db = Database(path)
# Store old value
old = db["cats"]
# Change value. Note that I use *my* twitter for testing, except when something
# might go wrong, in which case I use Moshe's.
db["cats"] = "database corruption wreaks havoc upon this earth"
# Test that the file was changed by making a new instance and reading
stored = Database(path)["cats"]
assert stored == "database corruption wreaks havoc upon this earth"
# Restore
db["cats"] = old
