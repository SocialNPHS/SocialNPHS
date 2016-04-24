""" Tests of twitter source """
import sys
sys.path.insert(0, ".")

# -- Tests of NPUser -- #
from SocialNPHS.sources.twitter import user
a = user.NPUser("1Defenestrator")
assert a.sex == "M"

print("All tests passed!")
