class TestSharedData:
    def test_shared_data_inside_class(self, shared_data_inside_class):
        test_case = shared_data_inside_class.get('test_cases')[0]
        status = test_case.get('status')
        assert status == 'passed'

    def test_shared_data_between_test_suites(self, shared_data_between_test_suites):
        test_case = shared_data_between_test_suites.get('test_cases')[0]
        status = test_case.get('status')
        assert status == 'passed'
