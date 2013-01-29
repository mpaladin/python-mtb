#! /usr/bin/python
"""
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 Copyright (C) 2013 CERN
"""

import test.all_tests
import unittest


def main():
    """ run the tests """
    test_suite = test.all_tests.create_test_suite()
    unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    main()