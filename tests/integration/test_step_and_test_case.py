from xayah_test.classes.step_and_test_case_classes import ClassStepAndTestCasePassed, ClassStepAndTestCaseFailed


class TestStepAndTestCase:

    # all passed steps makes test case passed
    def test_all_steps_passed(self, test_result):
        ClassStepAndTestCasePassed.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]
        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('status') == 'passed'

        step2 = steps[1]

        assert step2.get('status') == 'passed'

        assert test_case.get('status') == 'passed'

    # all one step is failed then test case is failed too
    def test_step_failed(self, test_result):
        ClassStepAndTestCaseFailed.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]
        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        step1 = steps[0]

        assert step1.get('status') == 'passed'

        step2 = steps[1]

        assert step2.get('status') == 'failed'

        assert test_case.get('status') == 'failed'
