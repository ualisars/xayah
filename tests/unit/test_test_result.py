from xayah_test.classes.test_result_classes import ClassResultTestPositive, ClassTestResultFailed


class TestTestResult:
    def test_add_test_case_class_name_and_method(self, test_result):
        class_name = "xayah_class"
        method_name = "xayah_method"
        status = "passed"
        name = f"{class_name}::{method_name}"

        test_result.add_test_case(class_name=class_name, method_name=method_name, status=status)

        test_case = test_result.get_test_case(name)

        assert test_case is not None, f"test case not found by name: {name}"
        assert test_case.get('class_name') == class_name
        assert test_case.get('method_name') == method_name
        assert test_case.get('status') == status
        assert test_case.get('name') == name

    def test_add_test_case_failed(self, test_result):
        class_name = "xayah_class"
        method_name = "xayah_method_failed"
        status = "failed"
        name = f"{class_name}::{method_name}"

        test_result.add_test_case(class_name=class_name, method_name=method_name, status=status)

        test_case = test_result.get_test_case(name)

        assert test_case is not None, f"test case not found by name: {name}"
        assert test_case.get('status') == status

    def test_add_step(self, test_result):
        step_name = 'authorization'
        step_status = 'passed'
        message = "all good"
        method_name = "xayah_method_step"
        category = 'step'

        test_result.add_step(
            name=step_name,
            method_name=method_name,
            message=message,
            category=category,
            status=step_status
        )

        steps = test_result.get_steps(method_name)

        assert len(steps) == 1, "step is not added"

        step = steps[0]

        assert step.get('name') == step_name
        assert step.get('status') == step_status
        assert step.get('message') == message
        assert step.get('category') == category

    def test_create_test_result_smoke(self, test_result):
        test_result_class_name = 'ClassResultTestPositive'
        ClassResultTestPositive.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test suite in test result"
        test_suite = result[0]

        class_name = test_suite.get('class_name')
        assert class_name == test_result_class_name

        test_cases = test_suite.get('test_cases')
        assert len(test_cases) == 1, "not exactly 1 test cases in test suite"

        test_case = test_cases[0]

        test_case_class_name = test_case.get('class_name')
        assert test_case_class_name == test_result_class_name

        test_case_method_name = test_case.get('method_name')
        assert test_case_method_name == 'test_math_positive'

        test_case_name = test_case.get('name')
        assert test_case_name == f'{test_case_class_name}::{test_case_method_name}'

        test_case_method = test_case.get('status')
        assert test_case_method == 'passed'

    def test_create_test_result_failed(self, test_result):
        ClassTestResultFailed.run_test_cases()
        result = test_result.create_test_result()

        assert len(result) == 1, "not exactly 1 test suite in test result"
        test_suite = result[0]

        class_name = test_suite.get('class_name')
        assert class_name == 'ClassTestResultFailed'

        test_cases = test_suite.get('test_cases')
        assert len(test_cases) == 1, "not exactly 1 test cases in test suite"

        test_case = test_cases[0]

        status = test_case.get('status')
        assert status == 'failed'

        assertion_message = test_case.get('assertion_message')

        assert assertion_message == '4 is not 5'
