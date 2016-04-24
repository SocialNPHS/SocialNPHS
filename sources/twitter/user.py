"""
Base class for a twitter user
"""

import json

import tweepy


# Retrieves Twitter API tokens & keys from cached JSON store
with open('token.json') as f:
    t = json.load(f)
    CONSUMER_KEY = t['CONSUMER_KEY']
    CONSUMER_SECRET = t['CONSUMER_SECRET']
    ACCESS_TOKEN = t['ACCESS_TOKEN']
    ACCESS_SECRET = t['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

with open('users.json') as f:
    Students = json.load(f)


class NPUser(object):
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.user_info = Students[self.screen_name]
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
        grade = Students[self.screen_name]['grade']
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

if __name__ == "__main__":
    a = NPUser("1Defenestrator")
    print(a.sex)
    print(a.grade)
