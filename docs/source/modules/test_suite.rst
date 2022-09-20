Test Suite
************************

TestSuite is a collection of test cases.

In xayah, test suite is represented by python class
decorated with TestSuite.init

.. code-block::
    :caption: example of test suite

    from xayah import TestSuite


    @TestSuite.init
    class TestAdd:
        def test_add(self):
            assert 1 + 2 == 3


Init
--------------

TestSuite.init makes a class runnable by xayah. It adds a
run_test_cases method to the class. So,
all test methods (methods with test prefix)
can be run using run_test_cases

.. code-block::
    :caption: all test methods will be executed

        TestAdd.run_test_cases()


Title
--------------

TestSuite.title(title: str) adds title to the test suite

.. code-block::
    :caption: title 'Add method' will be added to the test suite

        from xayah import TestSuite


        @TestSuite.init
        @TestSuite.title('Add method')
        class TestAdd:
            def test_add(self):
                assert 1 + 2 == 3


Before all
--------------

TestSuite.before_all(fn: Callable)
applies to a method in the test class. Makes the method
run before all other test methods. Code in that method
won't be included in the test result

.. code-block::
    :caption: method 'before' will be executed before all test methods

        from xayah import TestSuite


        @TestSuite.init
        class TestAdd:
            @TestSuite.before_all
            def before():
                # some code that need to run before tests
            def test_add(self):
                assert 1 + 2 == 3


After all
--------------

TestSuite.after_all(fn: Callable)
applies to a method in test class. Makes the method
run after all other test methods. Code in that method
won't be included in the test result

.. code-block::
    :caption: method 'clean' will be executed after all test methods

        from xayah import TestSuite


        @TestSuite.init
        class TestAdd:
            @TestSuite.after_all
            def clean():
                # some code that need to run after tests
            def test_add(self):
                assert 1 + 2 == 3
