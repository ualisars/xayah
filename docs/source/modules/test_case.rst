Test Case
************************

Test case is a set of preconditions, steps and
expected results developed to test particular outputs
or situations.

In xayah, test case is represented by python method
located in test suite and having test prefix.
In a current version test case
ought to be inside test suite

.. code-block::
    :caption: this is test case:

        from xayah import TestSuite


        @TestSuite.init
        class TestLogin:
        # test_login_empty is test case
        # as it has test prefix
        def test_login_empty(self):
            # check for empty fields in login


Title
-------------------------

TestCase.title(title: str) adds title to the test case

.. code-block::
    :caption: title 'Response time is less than 200ms' will be added to the test case

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestAPI:
            @TestCase.title('Response time is less than 200ms')
            def test_response_time(self):
                # check response check


Description
-------------------------

TestCase.description(description: str) adds description
to the test case

.. code-block::
    :caption: description 'check that champion can be found by their name' will be added to the test case

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestFilter
            @TestCase.description('check that champion can be found by their name')
            def test_filter_by_name(def):
                # check filter here


Link
-------------------------
TestCase.link(link: str) adds a link to the test case

.. code-block::
    :caption: link https://github.com/ualisars/xayah will be added to the test case

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestItems
            @TestCase.link('https://github.com/ualisars/xayah')
            def test_buy_item(def):
                # check buy item functionality here


Severity
-------------------------

TestCase(severity: str or SeverityLevel) adds severity level
to the test case

.. code-block::
    :caption: severity level 'critical' will be added to the test case from xayah import SeverityLevel

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestShop:
            @TestCase.severity(SeverityLevel.CRITICAL)
            def test_buying_in_game_currency(self):
                # check buying champion with blue essence here

note: severity level can be added with strings

.. code-block::
    :caption: this code will have the same effect as the code above:

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestShop:
            @TestCase.severity('critical')
            def test_buying_in_game_currency(self):
                # check buying champion with blue essence here


Skip
-------------------------

TestCase.skip(reason: str = '') allows to skip the test case

.. code-block::
    :caption: this test case will have status='fail' and reason='skin currently disable'

        from xayah import TestSuite, TestCase


        @TestSuite.init
        class TestXayahSkins:
            TestCase.skip(reason='skin is currently disabled')
            def test_buy_cosmic_dusk(self):
                # check buying the skin


Additional params
-------------------------

TestCase.add_additional_params(class: test_class, fn: test_method, additional_params: Dict[str, str])
adds additional params to the test case.
Additional params are used to add anything that
needs to be in test result
but not included by xayah library

.. code-block::
    :caption: additional param {'champion_name': 'Zed'} will be added to the test case and can be used in test result

        from xayah import TestSuite, TestCase


        def buy_champion(name):
            # buy champion
            return True

        @TestSuite.init
        class TestShop:
            def test_buying_champion(self):
                name = 'Zed'
                TestCase.add_additional_params(
                    TestShop,
                    TestShop.test_buying_champion,
                    {'champion_name': name}
                )
                assertTrue(buy_champion(name), 'champion is not bought')
