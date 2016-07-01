import os

import livejson

localdir = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(localdir, "users.json")
students = livejson.File(dbpath, pretty=True, sort_keys=True)
