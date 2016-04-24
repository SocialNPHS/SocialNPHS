"""
Finds possible Twitter accounts of NPHS students by finding other users
that follow or are followed by confirmed NPHS accounts.
"""

import json
import tweepy
from user import NPUser

# users = []

"""
This doesn't work. It hits the ratelimit extremely quickly, but I don't know of
any good way to deal with that.
"""
# try:
#    for x in Students:
#        student = NPUser(x)
#        for u in student.following:
#            if u in student.followers:
#                users.append(u)  # pls no ratelimit
#                print(u.screen_name)
# except tweepy.error.RateLimitError as e:
#    print('Oops. Hit the ratelimit.')  # damnit
# finally:
#    print(len(users))  # just for good measure
