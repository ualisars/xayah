class TestTestResult:
    def test_add_test_case_classname_and_method(self, test_result):
        classname = "xayah_class"
        method = "xayah_method"
        status = "passed"
        name = f"{classname}:{method}"

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
        name = f"{classname}:{method}"

        test_result.add_test_case(classname=classname, method=method, status=status)

        test_case = test_result.get_test_case(name)

        assert test_case is not None, f"test case not found by name: {name}"
        assert test_case.status == status

    def test_add_step(self, test_result):
        step_name = 'authorization'
        step_status = 'passed'
        message = "all good"
        method = "xayah_method_step"

        test_result.add_step(step_name, method, message, step_status)

        steps = test_result.get_step(method)

        assert len(steps) == 1, "step is not added"

        step = steps[0]

        assert step.get('name') == step_name
        assert step.get('status') == step_status
        assert step.get('message') == message
