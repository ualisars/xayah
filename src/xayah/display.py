class BColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CHECK_MARK = u'\u2713'
    CROSS_MARK = u'\u2717'


class Display:
    offset = '   '

    def __init__(self):
        self.all_test_cases = 0
        self.passed_test_cases = 0
        self.failed_test_cases = 0
        self.offset = '   '

    def display_test_result(self, test_suites) -> None:
        """
        display test result in console
        """
        result = ''
        result += Display.display_start()
        for key, value in test_suites.items():
            result += f'{key}:\n'
            test_cases = value.get('test_cases')
            result += self.display_test_cases(test_cases)

        result += self.display_statistics(result)

        print(result)

    def display_test_cases(self, test_cases: list) -> str:
        result_string = ''
        offset = self.offset
        for test_case in test_cases:
            test_case_method_name = test_case.get('method_name')
            test_case_status = test_case.get('status')
            self.all_test_cases += 1
            if test_case_status == 'passed':
                self.passed_test_cases += 1
                result_string += f'{offset}{test_case_method_name}  {BColor.OKGREEN}{BColor.CHECK_MARK}{BColor.ENDC}\n'
            else:
                self.failed_test_cases += 1
                result_string += f'{offset}{test_case_method_name}  {BColor.FAIL}{BColor.CROSS_MARK}{BColor.ENDC}\n'

            result_string += self.display_steps(test_case)

        return result_string

    def display_steps(self, test_case: dict) -> str:
        result_string = ''
        steps = test_case.get('steps')
        offset = self.offset * 2
        for step in steps:
            step_status = step.get('status')
            step_name = step.get('name')
            if step_status == 'passed':
                result_string += f'{offset}{step_name}  {BColor.OKGREEN}{BColor.CHECK_MARK}{BColor.ENDC}\n'
            else:
                result_string += f'{offset}{step_name}  {BColor.FAIL}{BColor.CROSS_MARK}{BColor.ENDC}\n'

        return result_string

    def display_statistics(self, result: str) -> str:
        statistics = f'test run is finished:\n {self.all_test_cases} is run\n {BColor.OKGREEN}{self.passed_test_cases} is passed\n {BColor.FAIL}{self.failed_test_cases} is failed{BColor.ENDC}\n'
        statistics += result
        return statistics

    @staticmethod
    def display_start():
        half = '==========================================================================='
        display_text = f'{half} start of the test session  {half}'
        return display_text
