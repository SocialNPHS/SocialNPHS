"""
Methods for getting NPHS tweets
"""

from datetime import datetime, timedelta

from tweepy import Cursor

from SocialNPHS.sources.twitter.auth import api


def get_nphs_tweets(since=datetime.utcnow() - timedelta(hours=24)):
    """ Get most recent tweets from the Twitter list of NPHS students """
    statuses = []

    # Find all tweets since the provided datetime
    for status in Cursor(api.list_timeline, "1Defenestrator", "NPHS").items():
        if status.created_at < since:
            break
        else:
            statuses.append(status)

    # statuses = api.list_timeline("1Defenestrator", "NPHS")
    # Filter out retweets and return
    return [s for s in statuses if not s.text.startswith("RT @")]
