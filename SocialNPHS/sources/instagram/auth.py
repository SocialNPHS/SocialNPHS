""" Instagram authentication and all """

import json

from instagram.client import InstagramAPI


def _get_secret_stuffs():
    """ Retrieves Instagram API token and secret """
    secrets = ["ACCESS_TOKEN", "CLIENT_SECRET"]
    with open("token.json") as f:
        t = json.load(f)
        return [t[s] for s in secrets]


def _get_api():
    """ Gets an Instagram API from authentication things """
    spoopy = _get_secret_stuffs()
    return InstagramAPI(access_token=spoopy[0], client_secret=spoopy[1])

api = _get_api()
