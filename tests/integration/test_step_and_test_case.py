from xayah_test.classes.step_and_test_case_classes import (
    ClassStepAndTestCasePassed,
    ClassStepAndTestCaseFailed,
    ClassStepAndTestCaseExecutionTime1Step,
    ClassStepAndTestCaseExecutionTime2Steps
)


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

    def test_step_execution_time(self, test_result):
        ClassStepAndTestCaseExecutionTime1Step.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 1, 'not exactly 1 step in test case'

        step = steps[0]

        start_time = step.get('start_time')
        end_time = step.get('end_time')
        execution_time = step.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert end_time > start_time

    def test_step_execution_time_2steps(self, test_result):
        ClassStepAndTestCaseExecutionTime2Steps.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        steps = test_case.get('steps')

        assert len(steps) == 2, 'not exactly 2 steps in test case'

        step1 = steps[0]

        start_time = step1.get('start_time')
        end_time = step1.get('end_time')
        execution_time = step1.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert end_time > start_time

        step2 = steps[0]

        start_time = step2.get('start_time')
        end_time = step2.get('end_time')
        execution_time = step2.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert end_time > start_time
