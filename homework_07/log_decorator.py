import inspect
import logging
import functools


class Log(object):
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'
    caller_func_message = 'Function {} called from function: {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwds):
            caller_name = inspect.currentframe().f_back.f_code.co_name
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))
            self.logger.info(self.caller_func_message.format(func.__name__, caller_name))
            f_result = func(*args, **kwds)
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))
            return f_result
        return wrapper