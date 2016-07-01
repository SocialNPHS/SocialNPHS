"""
Run all tests
"""
import glob
from os import path
import sys
import unittest

import coverage

localdir = path.dirname(path.abspath(__file__))

# Absolute path to each testing script
tests = glob.glob(path.join(localdir, "*.py"))
tests = set(tests) - set(["__main__.py", "__init__.py"])

# Names of modules to be imported
testNames = [path.splitext(path.split(t)[1])[0] for t in tests]

cov = coverage.Coverage(source=["SocialNPHS"])
cov.start()

suites = [unittest.defaultTestLoader.loadTestsFromName(t) for t in testNames]
fullsuite = unittest.TestSuite(suites)

unittest.TextTestRunner().run(fullsuite)

cov.stop()
if "--report-coverage" in sys.argv:
    print("\n")
    cov.report()
