from xayah_test import StepTestSmoke


class TestStep:
    def test_step_smoke(self, test_result):
        StepTestSmoke.run_test_cases()
        result = test_result.create_test_result()

