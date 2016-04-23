import csv
import json


def validate_data(data):
    """ Returns False if there are any empty values in the list """
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
        data["alias"] = None
    # Replace boolean protected values with Python bool
    data["protected"] = False if data["protected"] == "FALSE" else True

    return data


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
        row[categories.index("handle")]:
        process_data({categories[i]: n for i, n in enumerate(row)})
        for row in completerows
    }
    # --- Write JSON file --- #
    with open(out, "wb") as f:
        f.write(json.dumps(outdict, indent=2, sort_keys=True))

if __name__ == "__main__":
    csv2json("sources/twitter/users.csv", "sources/twitter/users.json")
