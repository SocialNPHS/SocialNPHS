"""
Run all tests
"""
import glob
import os
import sys
import unittest

import coverage

localdir = os.path.dirname(os.path.abspath(__file__))

# Absolute path to each testing script
tests = glob.glob(os.path.join(localdir, "*.py"))
tests = set(tests) - set(["__main__.py", "__init__.py"])

# Names of modules to be imported
testNames = [os.path.splitext(os.path.split(t)[1])[0] for t in tests]

cov = coverage.Coverage(source=["SocialNPHS"])
cov.start()

suites = [unittest.defaultTestLoader.loadTestsFromName(t) for t in testNames]
fullsuite = unittest.TestSuite(suites)

unittest.TextTestRunner().run(fullsuite)

cov.stop()
if "--report-coverage" in sys.argv:
    # Report coverage to either console or a build artifact, depending on
    # whether we're inside CircleCI
    inside_circle = "CIRCLE_ARTIFACTS" in os.environ
    # We are inside CircleCI
    if inside_circle:
        export = os.path.join(os.environ["CIRCLE_ARTIFACTS"], "coverage.txt")
        with open(export, "w") as f:
            cov.report(show_missing=True, file=f)
    else:
        cov.report(show_missing=True)
