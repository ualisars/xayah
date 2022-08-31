import logging


class ClassTestCasePassed:
    @staticmethod
    def test_test_case_passed():
        assert 1 == 1


class ClassTestCaseFailed:
    @staticmethod
    def test_test_case_failed():
        assert 1 == 2


class ClassTestCaseAssertionMessageEmpty:
    @staticmethod
    def test_test_case_assertion_message_empty():
        assert 10 == 2


class ClassTestCaseAssertionMessage:
    @staticmethod
    def test_test_case_assertion_message():
        assert 30 == 1, '30 is not 1'


class ClassTestCaseExecutionTimePassed:
    @staticmethod
    def test_execution_time():
        assert 1 == 1


class ClassTestCaseExecutionTimeFailed:
    @staticmethod
    def test_execution_time():
        assert 30 == 1


class ClassTestCaseLogsPrint:
    @staticmethod
    def test_print():
        print('start of assertions')
        assert 1 == 1
        print('end of assertions')


class ClassTestCaseLogging:
    @staticmethod
    def test_logging():
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        root.addHandler(handler)

        logging.basicConfig(level=logging.NOTSET)
        logger = logging.getLogger('test_logs_logger')
        logger.setLevel(logging.DEBUG)
        logger.info('start of assertion')
        assert 1 == 1
        logger.debug('end of assertion')


class ClassTestCasePrintAndLogging:
    @staticmethod
    def test_print_and_logging():
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        root.addHandler(handler)

        logging.basicConfig(level=logging.NOTSET)
        logger = logging.getLogger('test_print_and_logging')
        logger.setLevel(logging.DEBUG)
        print('print')
        assert 1 == 1
        logger.info('logging')


class ClassTestCaseAllLogging:
    @staticmethod
    def test_logging():
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        root.addHandler(handler)

        logging.basicConfig(level=logging.NOTSET)
        logger = logging.getLogger('test_all_logger')
        logger.setLevel(logging.DEBUG)
        logger.info('INFO')
        logger.debug('DEBUG')
        logger.warning('WARNING')
        logger.error('ERROR')
        logger.critical('CRITICAL')
        assert 1 == 1


class ClassTestCaseFailedAssertionPrint:
    @staticmethod
    def test_logging():
        print('failed')
        assert 1 == 2


class ClassTestCaseFailedAssertionLogging:
    @staticmethod
    def test_logging():
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        root.addHandler(handler)

        logging.basicConfig(level=logging.NOTSET)
        logger = logging.getLogger('test_logs_print_failed')
        logger.setLevel(logging.DEBUG)
        logger.info('failed')
        assert 1 == 2
