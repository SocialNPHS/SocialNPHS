# Tests
Tests of different parts of the library.

## Why
An important part of test-driven-development is that tests be thorough.
Therefore, every time someone adds something new, a test should be added to
make sure it works.

## Running tests
All tests can be run at once from the project root with `python3 tests`. This
will execute the `__main__.py` script.

#### File structure of `tests`
- There should be one testing script for each subpackage of SocialNPHS
(`sources`, `language`, etc.). These are already in place.
- For each single python script, there should a class inheriting from
`unittest.TestCase` placed in the appropriate testing file
- Use different `def` statements inside these tests as necessary
