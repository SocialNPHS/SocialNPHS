"""
Methods for getting NPHS tweets
"""

from SocialNPHS.sources.twitter.auth import api


def get_nphs_tweets():
    """ Get most recent tweets from the Twitter list of NPHS students """
    statuses = api.list_timeline("1Defenestrator", "NPHS")
    # Filter out retweets and return
    return [s for s in statuses if not s.text.startswith("RT @")]
