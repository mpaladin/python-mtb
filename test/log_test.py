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
import logging
import os
import shutil
import unittest

import mtb.log as log
from mtb.test import parametrized


LOG_OPERATIONS = "debug info warning error critical".split()

TEST_DIR = os.path.abspath("test_tmp")


class LogTest(unittest.TestCase):
    """ Test :py:mod:`mtb.log` utilities module. """

    def setUp(self):
        """ Setup the test environment for the log test. """
        # remove the test folder
        shutil.rmtree(TEST_DIR, True)
        # and create it again
        try:
            os.mkdir(TEST_DIR)
        except OSError:
            pass

    def tearDown(self):
        """ Restore the test environment and delete the test folder. """
        shutil.rmtree(TEST_DIR, True)

    @parametrized("log_n log_s".split(), log.LOG_SYSTEMS.items())
    def test_init(self, log_n, log_s):
        """ Test log system creation. """
        print("running log setup for %s" % (log_n,))
        extra = dict()
        if log_n == "file":
            extra = {
                "handler_options": {
                    "filename": os.path.join(TEST_DIR, "file.log"),
                }
            }
        log.setup_log("foo", log_n, extra=extra)
        print("...test log setup ok")

    @parametrized("log_n log_s".split(), log.LOG_SYSTEMS.items())
    def test_log_operations(self, log_n, log_s):
        """ Test log system operations. """
        print("running log operations checking for %s" % (log_n,))
        extra = dict()
        if log_n == "file":
            extra = {
                "handler_options": {
                    "filename": os.path.join(TEST_DIR, "file.log"),
                }
            }
        log.setup_log("foo", log_n, extra=extra)
        logger = logging.getLogger("foo")
        for operation in LOG_OPERATIONS:
            getattr(logger, operation)(
                "log test for %s.%s" % (log_n, operation))
        print("...test log operations checking ok")


if __name__ == "__main__":
    unittest.main()
