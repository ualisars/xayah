from xayah_test.classes.test_result_classes import ClassResultTestPositive, ClassTestResultFailed


class TestTestResult:
    def test_add_test_case_classname_and_method(self, test_result):
        classname = "xayah_class"
        method = "xayah_method"
        status = "passed"
        name = f"{classname}::{method}"

        test_result.add_test_case(classname=classname, method=method, status=status)

        test_case = test_result.get_test_case(name)

        assert test_case is not None, f"test case not found by name: {name}"
        assert test_case.get('classname') == classname
        assert test_case.get('method') == method
        assert test_case.get('status') == status
        assert test_case.get('name') == name

    def test_add_test_case_failed(self, test_result):
        classname = "xayah_class"
        method = "xayah_method_failed"
        status = "failed"
        name = f"{classname}::{method}"

        test_result.add_test_case(classname=classname, method=method, status=status)

        test_case = test_result.get_test_case(name)

        assert test_case is not None, f"test case not found by name: {name}"
        assert test_case.get('status') == status

    def test_add_step(self, test_result):
        step_name = 'authorization'
        step_status = 'passed'
        message = "all good"
        method = "xayah_method_step"

        test_result.add_step(step_name, method, message, step_status)

        steps = test_result.get_steps(method)

        assert len(steps) == 1, "step is not added"

        step = steps[0]

        assert step.get('name') == step_name
        assert step.get('status') == step_status
        assert step.get('message') == message

    def test_create_test_result_smoke(self, test_result):
        test_result_classname = 'ClassResultTestPositive'
        ClassResultTestPositive.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_scenario = result[0]

        classname = test_scenario.get('classname')
        assert classname == test_result_classname

        test_cases = test_scenario.get('test_cases')
        assert len(test_cases) == 1, "not exactly 1 test cases in test scenario"

        test_case = test_cases[0]

        test_case_classname = test_case.get('classname')
        assert test_case_classname == test_result_classname

        test_case_method = test_case.get('method')
        assert test_case_method == 'test_math_positive'

        test_case_name = test_case.get('name')
        assert test_case_name == f'{test_case_classname}::{test_case_method}'

        test_case_method = test_case.get('status')
        assert test_case_method == 'passed'

    def test_create_test_result_failed(self, test_result):
        ClassTestResultFailed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test scenario in test result"
        test_scenario = result[0]

        classname = test_scenario.get('classname')
        assert classname == 'ClassTestResultFailed'

        test_cases = test_scenario.get('test_cases')
        assert len(test_cases) == 1, "not exactly 1 test cases in test scenario"

        test_case = test_cases[0]

        status = test_case.get('status')
        assert status == 'failed'

        assertion_message = test_case.get('assertion_message')

        assert assertion_message == '4 is not 5'
