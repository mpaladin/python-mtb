"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Copyright (C) 2013 CERN
"""
import unittest

from mtb.string import u_, get_uuid


def some_function(**_):
    """ Example. """
    pass


class StringTest(unittest.TestCase):
    """ Test :py:mod:`mtb.string` utilities module. """

    def test_u_(self):
        """ Test get_uuid function. """
        u_("hello world!")

    def test_get_uuid(self):
        """ Test get_uuid function. """
        self.assert_(type(get_uuid()) == str)


if __name__ == "__main__":
    unittest.main()
