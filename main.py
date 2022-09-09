from xayah_test import CheckTestCase
from src.xayah.test_result import TestResult

CheckTestCase.run_test_cases()
result = TestResult().create_test_result()
print('result', result)
