import logging


class ExceptionLogger:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_logger = logging.getLogger('console_logger')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_logger.addHandler(console_handler)

    file_logger = logging.getLogger('file_logger')
    file_handler = logging.FileHandler('exceptions.log')
    file_handler.setFormatter(formatter)
    file_logger.addHandler(file_handler)

    def __init__(self, exception, log_type):
        self.exception = exception
        self.log_type = log_type

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exception as e:
                self.log_exception(e)

        return wrapper

    def log_exception(self, exception):
        if self.log_type == 'console':
            self.console_logger.exception(exception)
        elif self.log_type == 'file':
            self.file_logger.exception(exception)


