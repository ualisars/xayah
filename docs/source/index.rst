.. xayah documentation master file, created by
   sphinx-quickstart on Sat Sep 10 16:06:20 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to xayah's documentation!
=================================

Xayah is a testing tool with test report functionality.

Xayah allows to execute single or several test classes
(test suites) separately. After executing tests, test report is
generated and be parsed to HTML or passed to telegram bot message.


.. code-block::
   :caption: Example of simple test:

      from xayah import TestSuite, TestResult

      def add(a, b):
         return a + b

      @TestSuite.init
      class TestAdd:
         def test_add(self):
            assert add(2, 3) == 5

      # generating a test report
      TestAdd.run_test_cases()
      report = TestResult().create_test_result()

.. toctree::
   :maxdepth: 2
   :caption: Modules:

   modules/test_suite

   modules/test_case

   modules/test_result

   modules/step

   modules/shared_data