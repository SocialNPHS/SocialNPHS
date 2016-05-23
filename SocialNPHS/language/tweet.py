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
    for n, tok in enumerate(tokens):
        if tok.startswith('@'):
            handle = tok.strip("@")
            if handle in user.students:
                usr = user.NPUser(handle)
                tokens[n] = usr.fullname
            else:
                # TODO: replace with twitter alias
                pass
    return nltk.pos_tag(tokens)
