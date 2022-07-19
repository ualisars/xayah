from xayah_test.classes.check_classes import ClassCheckPassed, ClassCheckFailed


class TestCheck:
    def test_check_passed(self, test_result):
        passed_classname = 'ClassCheckPassed'
        ClassCheckPassed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_scenario = result[0]

        classname = test_scenario.get('classname')
        assert classname == passed_classname

        test_cases = test_scenario.get('test_cases')

        assert len(test_cases) == 1, 'not exactly 1 test case in test scenario'

        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('name') == 'check 1'

        assert step1.get('status') == 'passed'

        step2 = steps[1]

        assert step2.get('name') == 'check 2'

        assert step2.get('status') == 'passed'

    def test_previous_failed(self, test_result):
        smoke_classname = 'ClassCheckFailed'
        ClassCheckFailed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_scenario = result[0]

        classname = test_scenario.get('classname')
        assert classname == smoke_classname

        test_cases = test_scenario.get('test_cases')

        assert len(test_cases) == 1, 'not exactly 1 test case in test scenario'

        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 3, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('name') == 'check 1 passed'

        assert step1.get('status') == 'passed'

        step2 = steps[1]

        assert step2.get('name') == 'check 2 failed'

        assert step2.get('status') == 'failed'

        step3 = steps[2]

        assert step3.get('name') == 'check 3 passed'

        assert step3.get('status') == 'passed'
