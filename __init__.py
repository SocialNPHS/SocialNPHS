"""
SocialNPHS - aggregate data from New Paltz High School's students using their
social media accounts
"""

import sources.twitter

if __name__ == "__main__":
    from pprint import pprint
    pprint(sources.twitter.data)
