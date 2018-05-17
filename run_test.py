import unittest
import os
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


def search_path_pat(path, pattern, paths):
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            if f.startswith(pattern):
                paths.append(os.path.join(path, f))
            search_path_pat(os.path.join(path, f), pattern, paths)


def run_tests(path):
    pat, paths = "test", []
    search_path_pat(path, pat, paths)
    for path in paths:
        test = unittest.TestLoader().discover(path, "test*py")
        if is_running_under_teamcity():
            TeamcityTestRunner(verbosity=2).run(test)
        else:
            unittest.TextTestRunner(verbosity=2).run(test)


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    run_tests(path)
