""" Run all tests. """
import os

localdir = os.path.dirname(os.path.abspath(__file__))


def listTests(folder):
    """ List all the tests in a folder of tests (files that end with .py) """
    folder = os.path.abspath(folder)
    return [os.path.join(folder, i) for i in os.listdir(folder)
            if i.endswith(".py")]

testDirs = ["utils", "sources"]  # Subfolders in which tests are kept
absTestDirs = [os.path.join(localdir, td) for td in testDirs]
tests = sum([listTests(td) for td in absTestDirs], [])

for test in tests:
    with open(test) as f:
        code = compile(f.read(), test, 'exec')
        exec(code)
    print("Tests in {} passed!".format(os.path.split(test)[1]))
