""" Tests of twitter source """
import sys
sys.path.insert(0, ".")

# -- Tests of NPUser -- #
from SocialNPHS.sources.twitter import user
luke = user.NPUser("1Defenestrator")
# These tests make sure no error is thrown and check type;
# they don't actually check value because the value is flexible
assert isinstance(luke.followers, list)
assert isinstance(luke.following, list)
assert isinstance(luke.grade, str)
assert isinstance(luke.has_graduated, bool)
# Test magic method
assert luke.fullname == "Luke Taylor"
assert luke.sex == "M"

# Test has_graduated by manipulating the grade
moshe = user.NPUser("G4_Y5_3X")
moshe.user_info["grade"] = "3000"
assert moshe.has_graduated is False
moshe.user_info["grade"] = "2000"
assert moshe.has_graduated is True
moshe.user_info["grade"] = "2016"  # Reset the value
