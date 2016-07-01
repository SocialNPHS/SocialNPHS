""" Static data used by SocialNPHS. By "static" I don't mean it doesn't change,
but it comes from a file instead of (directly) from the internet """

from SocialNPHS.data import district_bounds

district = district_bounds.ShapeFileData().get_district_by_name(
    "New Paltz Central School District"
)
