import logging
from Constant import ZipperApp as zac


def getlogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        file_handler = logging.FileHandler(zac.logpath)
        formatter = logging.Formatter(zac.logfomrat)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger