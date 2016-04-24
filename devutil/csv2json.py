"""
Script used to generate JSON databases from CSV data. Outputs JSON in a format
like that found in sources/twitter/users.json
"""

import csv
import json


def validate_data(data, categories):
    """ Returns False if the list should not be included in the database,
    either because it is an incomplete entry or because the account is
    protected. """
    if data[categories.index("protected")] != "FALSE":
        return False
    return not any([not x for x in data])


def process_data(data):
    """ Make some modifications to enrich data for a student """
    # Add full name as a value
    data["fullname"] = " ".join([
        data["first"],
        data["last"]
    ])
    # Replace null aliases with Python None
    if data["alias"] == "null":
        data["alias"] = data["fullname"]
    # Replace boolean protected values with Python bool
    data["protected"] = False if data["protected"] == "FALSE" else True

    data["handle"] = data["handle"].lstrip("@")

    return data


def csv2json(inp, out):
    """ Read a CSV file, write a JSON file. Magic. """
    # --- Load the CSV file --- #
    with open(inp, "rt", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # --- Extract data --- #
    # Header, describes categories
    categories = [c.lower() for c in rows[0]]
    # Entries for whom we have a complete set of data. Exclude partial entries
    completerows = [r for r in rows[1:] if validate_data(r, categories)]

    # --- Make a dict --- #
    # Form a dict for output. Pairs the handle with a dict of all categories.
    outdict = {
        row[categories.index("handle")].lstrip("@"):
        process_data({categories[i]: n for i, n in enumerate(row)})
        for row in completerows
    }
    # --- Write JSON file --- #
    with open(out, "wt", encoding="utf-8") as f:
        f.write(json.dumps(outdict, indent=2, sort_keys=True))

if __name__ == "__main__":
    csv2json("SocialNPHS/sources/twitter/users.csv",
             "SocialNPHS/sources/twitter/users.json")
