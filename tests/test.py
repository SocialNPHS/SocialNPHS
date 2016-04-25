""" Run all tests. """
import os

localdir = os.path.dirname(os.path.abspath(__file__))


def listTests(folder):
    """ List all the tests in a folder of tests (files that end with .py) """
    folder = os.path.abspath(folder)
    return [os.path.join(folder, i) for i in os.listdir(folder)
            if i.endswith(".py")]

# All files in the same directory as this file
subfiles = [os.path.join(localdir, fi) for fi in os.listdir(localdir)]
# All directories inside the directory this file is in
testDirs = [d for d in subfiles if os.path.isdir(d)]
# Find tests in identified test directories, and flatten
tests = sum([listTests(td) for td in testDirs], [])

for test in tests:
    with open(test) as f:
        code = compile(f.read(), test, 'exec')
        exec(code)
    print("Tests in {} passed!".format(os.path.split(test)[1]))
