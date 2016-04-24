"""
Base class for a twitter user
"""

import json

import tweepy

# -------- HELPER METHODS -------- #


def _get_secret_stuffs():
    """ Retrieves Twitter API tokens & keys from stored secrets """
    secrets = ["CONSUMER_KEY",
               "CONSUMER_SECRET",
               "ACCESS_TOKEN",
               "ACCESS_SECRET"]
    with open("token.json") as f:
        t = json.load(f)
        return [t[s] for s in secrets]


def _get_api():
    """ Gets an authenticated tweepy API instance from stored JSON secrets """
    secrets = _get_secret_stuffs()
    auth = tweepy.OAuthHandler(*secrets[:2])
    auth.set_access_token(*secrets[2:])
    return tweepy.API(auth)


def get_users_dict():
    with open('users.json') as f:
        return json.load(f)


# -------- GLOBALS -------- #

API = _get_api()
students = get_users_dict()


# -------- MAIN CLASSES -------- #


class NPUser(object):
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.user_info = students[self.screen_name]
        self.User = API.get_user(self.screen_name)

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
        grade = self.user_info['grade']
        return {
            '2016': 'Senior', '2017': 'Junior',
            '2018': 'Sophomore', '2019': 'Freshman'
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
    a = NPUser("1Defenestrator")
    print(a.sex)
    print(a.grade)
