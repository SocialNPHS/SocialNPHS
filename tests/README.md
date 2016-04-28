# Tests
Tests of different parts of the library.

## Why
An important part of test-driven-development is that tests be thorough.
Therefore, every time someone adds something new, a test should be added to
make sure it works

## Running tests
All tests can be run at once via the `test.py` script found in this directory.

## Adding tests
To make sure tests are seen by the `test.py` script, place them not directly in
the `tests` directory, but in a subfolder inside `tests`.

#### File structure of `tests`
- There should be one testing script for each major source file in the project
- There should be one folder inside `tests` for each folder inside `SocialNPHS`
