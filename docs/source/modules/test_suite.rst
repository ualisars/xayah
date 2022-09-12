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


.. currentmodule:: src.xayah.test_suite
.. autoclass:: src.xayah.TestSuite
    :members:

