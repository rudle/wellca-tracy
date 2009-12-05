#!/usr/bin/python2.4
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script to run all unit tests in this package."""


import document_test
import model_test
import module_test_runner
import ops_test
import robot_abstract_test
import util_test


def RunUnitTests():
  """Runs all registered unit tests."""
  test_runner = module_test_runner.ModuleTestRunner()
  test_runner.modules = [
      document_test,
      model_test,
      ops_test,
      robot_abstract_test,
      util_test,
  ]
  test_runner.RunAllTests()


if __name__ == "__main__":
  RunUnitTests()
