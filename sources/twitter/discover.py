"""
Finds possible Twitter accounts of NPHS students by finding other users
that follow or are followed by confirmed NPHS accounts.
"""

import json
import tweepy
from user import NPUser

with open('users.json') as f:
    students = json.load(f)

users = []

# Time to break some ratelimits.
for x in students:
    student = NPUser(x)
    for u in student.following:
        # if they are in new paltz or just didn't say where they are
        if u.location is None or 'new paltz' in u.location.lower():
            if u in student.followers:
                users.append(u)
                print(u.screen_name)

print(len(users))  # just a quick test
