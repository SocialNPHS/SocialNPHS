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
    tokens = tknzr.tokenize(tweet.text)
    # replace handles with real names
    for n in range(0, len(tokens)):
        if tokens[n].startswith('@'):
            handle = tokens[n][1:]
            if handle in user.students:
                usr = user.NPUser(tokens[n][1:])
                tokens[n] = usr.fullname
            else:
                # TODO: replace with twitter alias
                pass
    return nltk.pos_tag(tokens)
