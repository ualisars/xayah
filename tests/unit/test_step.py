from xayah_test.classes.step_classes import ClassStepPassed, ClassStepFailed


class TestStep:
    def test_step_passed(self, test_result):
        passed_classname = 'ClassStepPassed'
        ClassStepPassed.run_test_cases()
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

        assert step1.get('name') == 'step one'

        assert step1.get('status') == 'passed'

    "if previous step failed next step is not run"
    def test_previous_step_failed(self, test_result):
        step_classname = 'ClassStepFailed'
        ClassStepFailed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_scenario = result[0]

        classname = test_scenario.get('classname')
        assert classname == step_classname

        test_cases = test_scenario.get('test_cases')

        assert len(test_cases) == 1, 'not exactly 1 test case in test scenario'

        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        passed_step = steps[0]

        assert passed_step.get('name') == 'passed step 1'

        assert passed_step.get('status') == 'passed'

        failed_step = steps[1]

        assert failed_step.get('name') == 'failed step'

        assert failed_step.get('status') == 'failed'
