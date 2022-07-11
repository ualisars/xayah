from tests import CheckString, CheckMath
from src import Step
from src.test_result import TestResult


# TestString.run_test_cases()
CheckString.run_test_cases({'name': 'DEV', 'environment': 'DEV'}, {'name': 'PROD', 'environment': 'PROD'})



# print('Forest')
TestResult().create_test_result()
# #
# def test_conct():
#     print('aaaa')
#     with Step("KKKKK"):
#         a = "v"
#         print('ssssssssssss')
#         assert a == 'ыыыыыыыыыыы'
#         # raise Exception('sssssss')
#
# test_conct()
