""" Static data used by SocialNPHS.

By "static" I don't mean it doesn't change, but that it comes from a file
instead of (directly) from the internet.

This includes:
- District bounds data
- The database of twitter users
- The SQLite database
and a python interface to each of these
"""

from SocialNPHS.data import district_bounds

_district_data = district_bounds.ShapeFileData()

# This first run is slow-ish
district = _district_data.get_district_by_name(
    "New Paltz Central School District"
)

# This second run takes less than 1% of that though, because of caching
district_shape = _district_data.get_shape_by_name(
    "New Paltz Central School District"
)
