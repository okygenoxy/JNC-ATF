#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import gzip
import shutil
import platform
import logging
import logging.handlers
from const import DEF_LOGGING_FORMATTER,DEF_DATE_FORMATTER

# Create a new class that inherits from RotatingFileHandler.
class CompressedRotatingFileHandler(logging.handlers.RotatingFileHandler):
    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d.gz" % (self.baseFilename, i)
                dfn = "%s.%d.gz" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.remove(dfn)
            # A file may not have been created if delay is True.
            if os.path.exists(self.baseFilename):
                os.rename(self.baseFilename, dfn)
            # Compress it.
            with open(dfn, 'rb') as f_in, gzip.open('{}.gz'.format(dfn), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                os.remove(dfn)
        if platform.python_version().strip() == '2.7.12':
            if not self.delay:
                self.stream = self._open()


class Logger(object):
    """
    Main class for logging module.
    """

    logger = logging.getLogger('ATF-LOGGING')
    logger.addHandler(logging.NullHandler())

    @classmethod
    def config(cls, log_file, default_log_dir='logs', file_level='DEBUG', rotate_size=5, rotate_count=5,
               console_output=False, console_level="DEBUG", compress_log=True):
        if not os.path.exists(default_log_dir):
            os.mkdir(default_log_dir)
        cls.logger = logging.getLogger(log_file)

        for h in cls.logger.handlers:
            if isinstance(h, logging.NullHandler):
                cls.logger.removeHandler(h)

        cls.logger.setLevel(file_level)
        log_file_path = '{log_dir}{name}'.format(log_dir=default_log_dir, name=log_file)
        if compress_log:
            cls.fh = CompressedRotatingFileHandler(log_file_path, mode='a',
                                                   maxBytes=int(rotate_size) * 1024 * 1024,
                                                   backupCount=int(rotate_count))
        else:
            cls.fh = logging.handlers.RotatingFileHandler(log_file_path, mode='a',
                                                          maxBytes=int(rotate_size) * 1024 * 1024,
                                                          backupCount=int(rotate_count))
        cls.fh.setLevel(file_level)
        formatter = logging.Formatter(DEF_LOGGING_FORMATTER, DEF_DATE_FORMATTER)
        cls.fh.setFormatter(formatter)
        cls.logger.addHandler(cls.fh)
        if console_output:
            cls.ch = logging.StreamHandler(sys.stdout)
            cls.ch.setLevel(console_level)
            cls.ch.setFormatter(formatter)
            cls.logger.addHandler(cls.ch)

    @classmethod
    def debug(cls, msg):
        if msg is not None:
            cls.logger.debug(msg)

    @classmethod
    def info(cls, msg):
        if msg is not None:
            cls.logger.info(msg)

    @classmethod
    def warning(cls, msg):
        if msg is not None:
            cls.logger.warning(msg)

    @classmethod
    def error(cls, msg):
        if msg is not None:
            cls.logger.error(msg)

    @classmethod
    def critical(cls, msg):
        if msg is not None:
            cls.logger.critical(msg)


log_config = Logger.config
debug = Logger.debug
info = Logger.info
warning = Logger.warning
error = Logger.error
critical = Logger.critical