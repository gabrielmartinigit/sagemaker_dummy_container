import io
import logging


def get_string_io_logger(log_stringio_obj, logger_name):
    # create logger
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s \t[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
    )
    logger.setLevel(logging.DEBUG)

    # add normal steam handler to display logs on screen
    io_log_handler = logging.StreamHandler()
    io_log_handler.setFormatter(formatter)
    logger.addHandler(io_log_handler)

    # create stream handler and initialise it with string io buffer
    string_io_log_handler = logging.StreamHandler(log_stringio_obj)
    string_io_log_handler.setFormatter(formatter)

    # add stream handler to logger
    logger.addHandler(string_io_log_handler)

    return logger
