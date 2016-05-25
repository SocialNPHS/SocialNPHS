"""
Identify other NPHS students based on their connections and geolocated tweets
"""

import random

import tweepy

from SocialNPHS.sources.twitter.auth import api
from SocialNPHS.sources.twitter import *


def discover_by_location(origin, num_users=20):
    """
    Discovers users based on profile location, not post geolocation.
    `num_users` defaults to 20 because I'm pretty sure 20 is when the ratelimit
    kicks in. It's late and I'm too lazy to check, but I think that's it.
    """
    users = random.sample(origin.following + origin.followers, num_users)
    np_users = []
    for u in users:
        if u.location is not None and 'New Paltz' in u.location:
            np_users.append(u.screen_name)
    return np_users


def discover_by_geolocation(origin, num_users=20):
    """
    Discovers users based on the location posted with some of their tweets.
    """
    users = random.sample(origin.following + origin.followers, num_users)
    np_users = []
    for u in users:
        # go through this user's tweets, searching for location info
        for t in api.user_timeline(u.id):
            if t.place is not None:
                # now we can do this the easy way...
                if t.place.attributes.postal_code is not None:
                    if t.place.attributes.postal_code == '12561':
                        np_users.append(u.screen_name)
                elif t.place.contained_within.name == 'New Paltz':
                    np_users.append(u.screen_name)
                # ...or the hard way:
                # check if the tweet's location's 4 coords are contained in
                # new paltz's general area
                # TODO: proabably a more mathematical way to figure this out,
                # such as using a `Polygon` object or something
                else:
                    for coord in t.place.bounding_box.coordinates[0][0]:
                        if coord[0] < -74.295 or coord[0] > -72.037 or
                        coord[1] < 41.655 or coord[1] > 41.811:
                            continue  # coord is outside of np area :'c
                        np_users.append(u.screen_name)
                        break
    return np_users

def discover_by_association(origin, num_users=20, num_np_followers=5):
    """
    Discovers users based on the number of `NPUser`s that follow them.
    """
    users = random.sample(origin.following, num_users)
    np_users = []
    for u in users:
        # go through this user's followers' followers to see how popular
        # they are with np students
        followers = u.followers
        if len(followers) > 2000:
            # nobody from new paltz would be super famous so we can skip them
            continue
        found_np_followers = 0
        for p in u.followers:
            if found_np_followers >= num_np_followers:
                # if `u` has enough np followers you win a new a car
                np_users.append(u.screen_name)
                break
            try:
                # check if this follower is an npuser
                _p = user.NPUser(p.screen_name)
            except ValueError:
                # well they aren't in the db so try the next dude
                continue
            else:
                found_np_followers += 1
    return np_users