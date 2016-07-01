import os.path

import shapefile

LOCALDIR = os.path.dirname(os.path.abspath(__file__))


class ShapeFileData(object):
    """ Representation of the data in the shapefile(s) """
    path_to_data = os.path.join(LOCALDIR, "tl_2015_36_unsd")

    def __init__(self):
        # Load the data
        self.reader = shapefile.Reader(self.path_to_data)

    @property
    def districts(self):
        """ Get a list of all districts """
        if not hasattr(self, "_districtcache"):
            self._districtcache = self.reader.shapeRecords()
        return self._districtcache

    def get_district_by_name(self, name):
        """ Get a district's geographic coordinates by its name """
        try:
            # District name is the third attribute
            return [x for x in self.districts if x.record[3] == name][0]
        except IndexError:
            raise IndexError(
                "District '{}' not found in NYS census records".format(name)
            )
