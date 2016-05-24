""" Run all tests. """
import glob
import os

localdir = os.path.dirname(os.path.abspath(__file__))


tests = glob.glob(os.path.join(localdir, "*/*.py"))

for test in tests:
    with open(test) as f:
        code = compile(f.read(), test, 'exec')
        exec(code)
    print("Tests in {} passed!".format(os.path.split(test)[1]))
