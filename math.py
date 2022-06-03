from tests import TestMath, TestString
from src.forest import Forest
# TestMath.run_test_cases()

for test_class in Forest().test_classes:
    test_class.run_test_cases()
