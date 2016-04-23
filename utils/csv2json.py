import csv
import json


def validate_data(data):
    """ Returns False if there are any empty values in the list """
    return not any([not x for x in data])


def csv2json(inp, out):
    """ Read a CSV file, write a JSON file. Magic. """
    # --- Load the CSV file --- #
    with open(inp, "rb") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # --- Extract data --- #
    # Header, describes categories
    categories = [c.lower() for c in rows[0]]
    # Entries for whom we have a complete set of data. Exclude partial entries
    completerows = [r for r in rows[1:] if validate_data(r)]

    # --- Make a dict --- #
    # Form a dict for output. Pairs the handle with a dict of all categories.
    outdict = {
        row[categories.index("handle")]:  # The handle, paired with
        {categories[i]: n for i, n in enumerate(row)}  # The dict w/ user info
        for row in completerows
    }
    # --- Write JSON file --- #
    with open(out, "wb") as f:
        f.write(json.dumps(outdict, indent=2, sort_keys=True))

if __name__ == "__main__":
    csv2json("sources/twitter/users.csv", "sources/twitter/users.json")
