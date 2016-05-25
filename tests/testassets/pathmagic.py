""" Magically change sys.path \o/"""

import sys
from os import path

# Project root
base = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../.."))
sys.path.insert(0, base)
