"""
Methods for getting NPHS tweets
"""

from SocialNPHS.sources.twitter.auth import api


def get_nphs_tweets():
    """ Get most recent tweets from the Twitter list of NPHS students """
    statuses = api.list_timeline("1Defenestrator", "NPHS")
    return [status.text for status in statuses]
