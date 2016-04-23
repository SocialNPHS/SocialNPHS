"""
Twitter data source. Fetches data from NPHS students' twitter accounts.
"""

import json
import os

# Directory in which this file is located
curdir = os.path.dirname(__file__)
# Path to JSON data file
datapath = os.path.join(curdir, "users.json")

with open(datapath) as f:
    data = json.loads(f.read())
