""" Run all tests. """
import glob
import unittest

from os import path

localdir = path.dirname(path.abspath(__file__))

# Absolute path to each testing script
tests = glob.glob(path.join(localdir, "tests/*.py"))

# Names of modules to be imported
testNames = ["tests." + path.splitext(path.split(t)[1])[0] for t in tests]

suites = [unittest.defaultTestLoader.loadTestsFromName(t) for t in testNames]
fullsuite = unittest.TestSuite(suites)
unittest.TextTestRunner().run(fullsuite)
