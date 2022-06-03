from tests import TestMath, TestString
from src.forest import Forest


TestMath.run_test_cases()
TestString.run_test_cases()



print('Forest')
Forest().create_test_result()
