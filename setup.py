from setuptools import setup
import sys

# Assert Python 3
if sys.version_info.major < 3:
    print("Requires Python 3")
    sys.exit(1)

setup(
    name="SocialNPHS",
    version="0.1",
    description="",
    author="Luke Taylor and Moshe Katzin-Nystrom",
    author_email="luke@deentaylor.com",
    url="http://luke.deentaylor.com/",
    install_requires=[
        "livejson",
        "tweepy",
        "shapely",
        "livejson"
    ],
    test_requires=[
        "coverage"
    ]
)
