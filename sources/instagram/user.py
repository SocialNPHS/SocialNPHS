"""
Base class for an instagram user
"""

import datetime
import json

from auth import api

# -------- HELPER METHODS -------- #


def get_users_dict():
    """ Loads the JSON file full of user info """
    with open('users.json') as f:
        return json.load(f)


def get_graduating_class():
    """Get the year of the next graduating class. Assumes once July starts,
    everyone moves up a grade, since people graduate in late June."""
    now = datetime.date.today()
    if now.month < 7:  # It's before summer (july)
        return now.year
    else:
        return now.year + 1


# -------- GLOBALS -------- #

students = get_users_dict()


# -------- MAIN CLASSES -------- #


class NPUser(object):
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.user_info = students[self.screen_name]
        self.User = api.user_search(self.screen_name, 1)[0]

    @property
    def following(self):
        """ List of users that this user follows """
        follows, next_ = api.user_follows(self.User.id)
        while next_:
            also_follows, next_ = api.user_follows(self.User.id,
                                                   with_next_url=next_)
            follows.extend(also_follows)
        return follows

    @property
    def followers(self):
        """ List of users following this user """
        followed, next_ = api.user_followed_by(self.User.id)
        while next_:
            also_followed, next_ = api.user_followed_by(self.User.id,
                                                        with_next_url=next_)
            followed.extend(also_followed)
        return followed

    @property
    def grade(self):
        """ Returns colloquial grade name of user """
        grade = int(self.user_info['grade'])
        grad = get_graduating_class()
        return {
            grad: 'Senior', grad + 1: 'Junior',
            grad + 2: 'Sophomore', grad + 3: 'Freshman'
        }.get(grade, None)

    def __getattr__(self, key):
        """ Magic method for automatically making user dict info accessible as
        an attribute"""
        if key not in self.user_info:
            raise AttributeError(self.__class__.__name__ +
                                 "instance has no attribute '" + key + "'")
        else:
            return self.user_info[key]


# -------- TESTS -------- #

if __name__ == "__main__":
    a = NPUser("dynasty_brave")
    print(a.sex)
    print(a.grade)

    b = NPUser("mhlkn")
    print(b.sex)
    print(b.grade)

    print(get_graduating_class())
