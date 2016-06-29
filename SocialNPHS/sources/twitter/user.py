"""
Base class for a twitter user
"""

import datetime
import os

import livejson

from SocialNPHS.sources.twitter.auth import api

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
students = livejson.Database(dbpath)

# -------- MAIN CLASSES -------- #


class User(object):
    """ Base class for a twitter user """
    def __init__(self, screen_name, should_retrieve=False):
        self.retrieved = False  # Has the API call been made to retrieve info?
        self.screen_name = screen_name

    @property
    def tweepy(self):
        """ Return the tweepy object for this user """
        # Store the tweepy object if it has not yet been stored
        if not self.retrieved:
            self._tweepy = api.get_user(self.screen_name)
            self.retrieved = True

        return self._tweepy

    @property
    def following(self):
        """ All the users this user follows """
        return self.tweepy.friends()

    @property
    def followers(self):
        """ All the users who follow this user """
        return self.tweepy.followers()


class NPUser(User):
    def __init__(self, screen_name):
        super(NPUser, self).__init__(screen_name)
        if self.screen_name not in students:
            # TODO: add the user to the database in this case
            raise ValueError("{} doesn't appear to be in the database".format(
                self.screen_name
            ))
        self.user_info = students[self.screen_name]

    @property
    def grade(self):
        """ Returns colloquial grade name of user """
        grade = int(self.user_info['grade'])
        grad = get_graduating_class()
        return {
            grad: 'Senior', grad + 1: 'Junior',
            grad + 2: 'Sophomore', grad + 3: 'Freshman'
        }.get(grade)

    @property
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
