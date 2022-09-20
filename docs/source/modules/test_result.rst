Test Result
************************

TestResult is a singleton class
that stores all information about executed tests.


Attributes:
---------------------------

    - test classes: list of all classes that have been decorated with TestSuite
    - test cases: all test methods of a particular class
    - test suites: represents all classes that have been executed
    - steps: steps of a test case


Create test result
--------------------------

TestResult().create_test_result generates test result
with test result schema described below:


Test result schema
-------------------------------

.. list-table:: Test Result

    * - №
      -
      -
      -
      - field name
      - description
      - type
      - example
    * - 1
      -
      -
      -
      - test class
      - class_name to TestSuite mapping
      - Dict[str, TestSuiteObject]
      - {TestShop: {'classname': 'TestShop', ...}}
    * - 1
      - 1
      -
      -
      - class_name
      - name of the class associated with the test suite
      - string
      - TestShop
    * - 1
      - 2
      -
      -
      - title
      - test suite's title
      - string
      - Shop
    * - 1
      - 3
      -
      -
      - test_cases
      - test cases that are linked to the test suite
      - List[TestCaseObject]
      -
    * - 1
      - 3
      - 1
      -
      - name
      - combination of class_name and method_name separated by '::'
      - string
      - TestShop::test_filter_champion_by_name
    * - 1
      - 3
      - 2
      -
      - class_name
      - name of the parent class
      - string
      - TestShop
    * - 1
      - 3
      - 3
      -
      - method_name
      - name of the test method
      - string
      - test_filter_champion_by_name
    * - 1
      - 3
      - 4
      -
      - status
      - status of the test case, possible values: passed, failed, skipped
      - string
      - passed
    * - 1
      - 3
      - 5
      -
      - assertion_message
      - message printed in false assertion
      - string
      - response time is more than 500ms
    * - 1
      - 3
      - 6
      -
      - assertion
      - assertion itself
      - string
      - 3 == 5
    * - 1
      - 3
      - 6
      -
      - severity_level
      - possible values: blocker, critical, normal, minor, trivial
      - string
      - critical
    * - 1
      - 3
      - 7
      -
      - start_time
      - start of the test case in seconds since the Epoch
      - float
      - 1663590332.0333679
    * - 1
      - 3
      - 8
      -
      - end_time
      - end of the test case in seconds since the Epoch
      - float
      - 1663590332.0333695
    * - 1
      - 3
      - 9
      -
      - execution_time
      - time required to execute test case in milliseconds
      - float
      - 0.0016689300537109375
    * - 1
      - 3
      - 10
      -
      - reason
      - reason to skip test case or why it is expected to fail
      - string
      - functionality not been implemented yet
    * - 1
      - 3
      - 11
      -
      - additional_params
      - any additional data that user wants to add to test case
      - Dict
      - {'platform': 'mobile'}
    * - 1
      - 3
      - 12
      -
      - steps
      - test case's steps
      - List[Step]
      -
    * - 1
      - 3
      - 12
      - 1
      - name
      - name of the step
      - string
      - API request
    * - 1
      - 3
      - 12
      - 2
      - status
      - step's status: passed or failed
      - string
      - passed
    * - 1
      - 3
      - 12
      - 3
      - category
      - which category step belongs to (step or check)
      - string
      - check
    * - 1
      - 3
      - 12
      - 3
      - message
      - reason why this step is failed
      - string
      - status code is not 200
    * - 1
      - 3
      - 12
      - 4
      - start_time
      - start of the step in seconds since the Epoch
      - float
      - 1663590332.0337355
    * - 1
      - 3
      - 12
      - 5
      - end_time
      - end of the step in seconds since the Epoch
      - float
      - 1663590332.0337377
    * - 1
      - 3
      - 12
      - 6
      - execution_time
      - time required to execute step in milliseconds
      - float
      - 0.0021457672119140625
