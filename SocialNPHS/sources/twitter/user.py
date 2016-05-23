"""
Base class for a twitter user
"""

import datetime
import json
import os

from SocialNPHS.sources.twitter.auth import api
from SocialNPHS.utils.database import Database

# -------- HELPER METHODS -------- #


def get_graduating_class():
    """Get the year of the next graduating class. Assumes once July starts,
    everyone moves up a grade, since people graduate in late June."""
    now = datetime.date.today()
    if now.month < 7:  # It's before summer (july)
        return now.year
    else:
        return now.year + 1

# -------- GLOBALS -------- #

localdir = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(localdir, "users.json")
students = Database(dbpath)

# -------- MAIN CLASSES -------- #


class NPUser(object):
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.user_info = students.get(self.screen_name)
        self.User = api.get_user(self.screen_name)

    @property
    def following(self):
        """ List of users that this user follows """
        return self.User.friends()

    @property
    def followers(self):
        """ List of users following this user """
        return self.User.followers()

    @property
    def grade(self):
        """ Returns colloquial grade name of user """
        grade = int(self.user_info['grade'])
        grad = get_graduating_class()
        return {
            grad: 'Senior', grad + 1: 'Junior',
            grad + 2: 'Sophomore', grad + 3: 'Freshman'
        }.get(grade)

    def has_graduated(self):
        """ Has the user graduated? """
        return int(self.user_info['grade']) < get_graduating_class()

    def __getattr__(self, key):
        """ Magic method for automatically making user dict info accessible as
        an attribute"""
        if key not in self.user_info:
            raise AttributeError(self.__class__.__name__ +
                                 "instance has no attribute '" + key + "'")
        else:
            return self.user_info[key]
