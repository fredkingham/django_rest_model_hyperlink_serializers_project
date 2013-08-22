#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

for i in sys.path:
    print i

import django
from django.conf import settings
from django.test.utils import get_runner


def usage():
    return """
    Usage: python runtests.py [UnitTestClass].[method]

    You can pass the Class name of the `UnitTestClass` you want to test.

    Append a method name if you only want to test a specific method of that class.
    """


def main():
    TestRunner = get_runner(settings)

    test_runner = TestRunner()
    if len(sys.argv) == 2:
        test_case = '.' + sys.argv[1]
    elif len(sys.argv) == 1:
        test_case = ''
    else:
        print(usage())
        sys.exit(1)
    test_module_name = 'hyperlinked_relational_serializer.hl_relational_serializer_tests'
    # if django.VERSION[0] == 1 and django.VERSION[1] < 6:
        # test_module_name = 'hyperlinked_relational_serializer.hl_relational_serializer_tests'

    failures = test_runner.run_tests([test_module_name])

    sys.exit(failures)

if __name__ == '__main__':
    main()
