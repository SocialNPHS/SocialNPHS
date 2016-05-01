"""
Given a tweet, tokenize it and shit.
"""

import json

import tweepy
import nltk
from nltk.tokenize import TweetTokenizer

from SocialNPHS.sources.twitter.auth import api
from SocialNPHS.sources.twitter import user
from SocialNPHS.utils.database import Database


def get_tweet_tags(tweet):
    """ Break up a tweet into individual word parts """
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(tweet.text)
    # replace handles with real names
    for n in range(0, len(tokens)):
        if tokens[n].startswith('@'):
            # TODO: account for case if mentioned user is not in users.json
            usr = user.NPUser(tokens[n][1:])
            tokens[n] = usr.fullname
    return nltk.pos_tag(tokens)
