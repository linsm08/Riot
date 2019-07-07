# -*- coding: utf-8 -*-

class LogPercentilesException(Exception):
    pass

class InvalidRawLogException(LogPercentilesException):
    def __init__(self, raw_log, *args, **kwargs):
        super(InvalidRawLogException, self).__init__(*args, **kwargs)
        self._raw_log = raw_log

    @property
    def raw_log(self):
        return self._raw_log
