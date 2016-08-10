"""
Run all tests
"""
import glob
import json
import os
import sys
import unittest

import coverage
import xmlrunner

# GLOBALS ---------------------------------------------------------------------
localdir = os.path.dirname(os.path.abspath(__file__))
inside_circle = "CIRCLECI" in os.environ


# SETUP -----------------------------------------------------------------------

# On personal computers, .gitignored JSON files can be more convenient than
# environment variables. If the "token.json" file is present, we copy its
# values as environment variables
tokenpath = os.path.join(localdir, "../token.json")
if os.path.exists(tokenpath):
    with open(tokenpath, "r") as f:
        data = json.load(f)
        os.environ.update(data)


# ASSEMBLE TESTS --------------------------------------------------------------

# Absolute path to each testing script
tests = glob.glob(os.path.join(localdir, "*.py"))
tests = set(tests) - set(["__main__.py", "__init__.py"])

# Names of modules to be imported
testNames = [os.path.splitext(os.path.split(t)[1])[0] for t in tests]


# RUN TESTS + REPORT ----------------------------------------------------------

# Start coverage reporter
cov = coverage.Coverage(source=["SocialNPHS"])
cov.start()

suites = [unittest.defaultTestLoader.loadTestsFromName(t) for t in testNames]
fullsuite = unittest.TestSuite(suites)

if inside_circle:
    # We're inside CircleCI. In this case, we output a rich HTML coverage
    # report to the build artifacts section, and we provide JUnit-style XML
    # reports for Circle to read.
    xmlrunner.XMLTestRunner(
        output=os.environ["CIRCLE_TEST_REPORTS"]
    ).run(fullsuite)
    cov.stop()
    out = os.path.join(os.environ["CIRCLE_ARTIFACTS"], "coverage-report")
    cov.html_report(directory=out)
    cov.save()
else:
    # We're running locally. Use a simpler test runner, and only report
    # coverage if it's explicitly requested via the --report-coverage line.
    unittest.TextTestRunner().run(fullsuite)
    cov.stop()
    # Report coverage if the flag is enabled
    if "--report-coverage" in sys.argv:
        print("\n")
        cov.report(show_missing=True)
        cov.save()
