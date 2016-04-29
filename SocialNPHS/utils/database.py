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

    def pop(self, key):
        self.jsonstore.pop(key)
        self.update()

    def get(self, *args):
        return self.jsonstore.get(*args)

    def __getitem__(self, key):
        return self.jsonstore[key]

    def __setitem__(self, key, value):
        self.jsonstore[key] = value
        self.update()

    def __len__(self):
        return len(self.jsonstore)
