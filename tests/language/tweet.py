""" Tests twitter language thing """
import sys
sys.path.insert(0, ".")

from SocialNPHS.language import tweet
from SocialNPHS.sources.twitter import user

a = user.NPUser("G4_Y5_3X")
print(tweet.get_tweet_tags(a.User.status))
