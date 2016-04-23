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
