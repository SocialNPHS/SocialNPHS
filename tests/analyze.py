"""
Unit tests for the portion of this project which performs the final analyses of
processed data.
"""

import unittest

# Magically manipulate sys.path
from testassets import pathmagic


class TestNotImplemented(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(NotImplementedError):
            import SocialNPHS.analyze
