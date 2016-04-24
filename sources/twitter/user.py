"""
Base class for a twitter user
"""

import json
import tweepy

# Retrieves Twitter API tokens & keys
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

    @property
    def sex(self):
        """ What do you think it returns? """
        return Students[self.screen_name]['sex']
