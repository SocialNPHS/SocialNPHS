"""
Given a tweet, tokenize it and shit.
"""

import nltk
from nltk.tokenize import TweetTokenizer

from SocialNPHS.sources.twitter.auth import api
from SocialNPHS.sources.twitter import user


def get_tweet_tags(tweet):
    """ Break up a tweet into individual word parts """
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(tweet)
    # replace handles with real names
    for n, tok in enumerate(tokens):
        if tok.startswith('@'):
            handle = tok.strip("@")
            if handle in user.students:
                # If we have a database entry for the mentioned user, we can
                # easily substitute a full name.
                usr = user.NPUser(handle)
                tokens[n] = usr.fullname
            else:
                # If there is no database entry, we use the user's alias. While
                # this is the full name in many cases, it is often not reliable
                usr = api.get_user(handle)
                tokens[n] = usr.name
    return nltk.pos_tag(tokens)
