"""
Given a tweet, tokenize it and shit.
"""

import nltk
from nltk.tag import util
from nltk.tokenize import sent_tokenize, TweetTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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


def tweet_connotation(tweet):
    """ Decide whether a tweet is generally positive or negative """
    anlyzr = SentimentIntensityAnalyzer()
    # break tweet up into sentences and analyze each seperately
    twtcontent = sent_tokenize(tweet)
    overall = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
    for s in twtcontent:
        scores = anlyzr.polarity_scores(s)
        # tally up each sentence's overall tone
        for i, z in enumerate(scores):
            overall[z] += scores[z]
    # average it all together for the tweet as a whole
    for v in overall:
        overall[v] = round(overall[v] / len(twtcontent), 3)
    return overall


def person_connotation(tweet, name):
    """
    Decide whether a person is talked favorably about or not, based on the
    tone of the sentences in which their name appears
    """
    twtcontent = sent_tokenize(tweet)
    overall = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
    mentions = 0
    # analyze each sentence talking about `name` person
    for s in twtcontent:
        tags = get_tweet_tags(s)
        # if the name appears in the tagged sentence, get its tone
        if (name, 'NNP') in tags:
            sentence = util.untag(tags)
            scores = tweet_connotation(' '.join(sentence))
            # add it up to the overall tweet's tone
            for i, z in enumerate(scores):
                overall[z] += scores[z]
            mentions += 1
    # averaging all sentences' scores. don't wanna divide by zero now do we
    if mentions != 0:
        for v in overall:
            overall[v] = round(overall[v] / mentions, 3)
    return overall


def person_multi_connotation(tweets, name):
    """ Analyze many tweets (a list of tweets in fact) about a person """
    mentioned = 0
    overall = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
    for t in tweets:
        score = person_connotation(t, name)
        for i, z in enumerate(score):
            if z != 0:
                mentioned += 1
                break
        for i, z in enumerate(score):
            overall[z] += score[z]
    if mentioned != 0:
        for v in overall:
            overall[v] = round(overall[v] / mentioned, 3)
    return overall
