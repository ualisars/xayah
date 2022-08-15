from xayah_test.classes.check_classes import ClassCheckPassed, ClassCheckFailed


class TestCheck:
    def test_check_passed(self, test_result):
        passed_class_name = 'ClassCheckPassed'
        ClassCheckPassed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result.keys()) == 1, "not exactly 1 test suite in test result"
        test_suite = result.get(passed_class_name)

        class_name = test_suite.get('class_name')
        assert class_name == passed_class_name

        test_cases = test_suite.get('test_cases')

        assert len(test_cases) == 1, 'not exactly 1 test case in test scenario'

        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('name') == 'check 1'

        assert step1.get('status') == 'passed'

        assert step1.get('category') == 'check'

        step2 = steps[1]

        assert step2.get('name') == 'check 2'

        assert step2.get('status') == 'passed'

        assert step2.get('category') == 'check'

    def test_previous_failed(self, test_result):
        smoke_class_name = 'ClassCheckFailed'
        ClassCheckFailed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_suite = result.get(smoke_class_name)

        class_name = test_suite.get('class_name')
        assert class_name == smoke_class_name

        test_cases = test_suite.get('test_cases')

        assert len(test_cases) == 1, 'not exactly 1 test case in test scenario'

        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 3, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('name') == 'check 1 passed'

        assert step1.get('status') == 'passed'

        assert step1.get('category') == 'check'

        step2 = steps[1]

        assert step2.get('name') == 'check 2 failed'

        assert step2.get('status') == 'failed'

        assert step2.get('category') == 'check'

        step3 = steps[2]

        assert step3.get('name') == 'check 3 passed'

        assert step3.get('status') == 'passed'

        assert step3.get('category') == 'check'
