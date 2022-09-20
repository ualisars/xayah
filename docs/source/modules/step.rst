Steps
************************

Step represents test case's steps.

There are two types of steps: step itself and check:

In step, execution of the test case terminated when
step is failed.

In check, execution of the test case isn't terminated
when check is failed.


Step
--------------------------

.. code-block::
    :caption: steps: model validation and check for empty response will not be executed

        from xayah import TestSuite, Step

        @TestSuite.init
        class TestAPI:
            def test_google(self):
                with Step('API request'):
                    # API request here
                    assert 1 == 2
                    # execution of the test case
                    # will be terminated as
                    # step is failed
                with Step('model validation'):
                    # model checking here
                with Step('check for empty response'):
                    # check for length of the body


Check
--------------------------

.. code-block::
    :caption: steps: model validation and check for empty response will be executed

        from xayah import TestSuite, Check

        @TestSuite.init
        class TestAPI:
            def test_google(self):
                with Check('API request'):
                    # API request here
                    assert 1 == 2
                    # execution of the test case
                    # will be continued
                    # even though check is failed
                with Check('model validation'):
                    # model checking here
                with Check('check for empty response'):
                    # check for length of the body

