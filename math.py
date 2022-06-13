from tests import TestMath, TestString
from src import Step
from src.forest import Forest


# TestString.run_test_cases()
TestString.run_test_cases({'name': 'DEV', 'environment': 'DEV'}, {'name': 'PROD', 'environment': 'PROD'})



# print('Forest')
Forest().create_test_result()
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
