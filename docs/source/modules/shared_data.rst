Shared Data
************************

Shared data is used to pass data among test suites

.. code-block::
    :caption:
        from xayah import TestSuite, SharedData
        @TestSuite.init
        class AddUserTest:
            @TestSuite.before_all
            def login(self):
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                # pass driver to test methods
                SharedData.share('driver', driver, scope='module')

                login_page = LoginPage(driver=driver)
                # login to website

            @TestSuite.after_all
            def close_driver(self):
                # get driver from shared data
                driver = SharedData.get('driver')
                driver.close()

            def test_add_user(self):
                # get driver from shared data
                driver = SharedData.get('driver')
                user_page = UserPage(driver=driver)
                # test user page
