"""
Easy way to read and write JSON databases
"""

import json


class Database(object):
    """ Class for writing JSON data as it is manipulated """
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as f:
            self.jsonstore = json.load(f)

    def update(self):
        """ Update the JSON database """
        with open(self.path, "w") as f:
            f.write(json.dumps(self.jsonstore, indent=2, sort_keys=True))

    def __getitem__(self, key):
        return self.jsonstore[key]

    def __setitem__(self, key, value):
        self.jsonstore[key] = value
        self.update()


if __name__ == "__main__":
    # -- Test changing the database, then restore -- #
    path = "sources/twitter/users.json"
    # Create magical database class
    db = Database(path)
    # Store old value
    old = db["G4_Y5_3X"]
    # Change value. Note that I use *my* twitter for testing, except when
    # something might go wrong, in which case I use Moshe's.
    db["G4_Y5_3X"] = "database corruption wreaks havoc on the earth"
    # Test that the file was changed by making a new instance and reading
    print(Database(path)["G4_Y5_3X"])
    # Restore
    db["G4_Y5_3X"] = old
