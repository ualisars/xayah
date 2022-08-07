from xayah_test.classes.check_and_test_case import (
    ClassChecksAndTestCasePassed,
    ClassCheckAndTestCaseFailed,
    ClassAtLeastOneCheckAndTestCaseFailed,
    ClassCheckAndTestCaseExecutionTime,
    ClassCheckAndTestCaseExecutionTime2Checks
)


class TestCheckAndTestCase:

    # all passed checks makes test case passed
    def test_all_checks_passed(self, test_result):
        ClassChecksAndTestCasePassed.run_test_cases()
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

    # if check failed test case should be failed too
    def test_one_check_failed(self, test_result):
        ClassCheckAndTestCaseFailed.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]
        steps = test_case.get('steps')

        assert len(steps) == 1, 'not exactly 1 steps in test case'

        step = steps[0]

        assert step.get('status') == 'failed'

        assert test_case.get('status') == 'failed'

    # if at least one check is failed so test case if failed too
    def test_at_least_one_check_failed(self, test_result):
        ClassAtLeastOneCheckAndTestCaseFailed.run_test_cases()
        result = test_result.create_test_result()

        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]
        steps = test_case.get('steps')

        assert len(steps) == 3, 'not exactly 3 steps in test case'

        step1 = steps[0]
        assert step1.get('status') == 'passed'

        step2 = steps[1]
        assert step2.get('status') == 'failed'

        step3 = steps[2]
        assert step3.get('status') == 'passed'

        assert test_case.get('status') == 'failed'

    def test_step_execution_time(self, test_result):
        ClassCheckAndTestCaseExecutionTime.run_test_cases()
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
        assert (end_time - start_time) * 1000 == execution_time, 'execution time not in milliseconds'
        assert end_time > start_time

    def test_step_execution_time_2steps(self, test_result):
        ClassCheckAndTestCaseExecutionTime2Checks.run_test_cases()
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
        assert (end_time - start_time) * 1000 == execution_time, 'execution time not in milliseconds'
        assert end_time > start_time

        step2 = steps[0]

        start_time = step2.get('start_time')
        end_time = step2.get('end_time')
        execution_time = step2.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert (end_time - start_time) * 1000 == execution_time, 'execution time not in milliseconds'
        assert end_time > start_time
