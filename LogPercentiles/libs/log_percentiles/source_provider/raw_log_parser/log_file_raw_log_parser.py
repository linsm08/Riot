# -*- coding: utf-8 -*-

from LogPercentiles.libs.log_percentiles.common.log import Log
from LogPercentiles.libs.log_percentiles.common.exception import InvalidRawLogException
from LogPercentiles.libs.log_percentiles.source_provider.raw_log_parser.raw_log_parser import RawLogParser

class LogFileRawLogParser(RawLogParser):
    def build_log(self, raw_log):
        if not raw_log:
            raise InvalidRawLogException(raw_log=raw_log)

        segs = raw_log.split(" ")
        response_time = None
        try:
            response_time = int(segs[-1])
        except IndexError as ex:
            raise InvalidRawLogException(raw_log=raw_log)
        except ValueError as ex:
            raise InvalidRawLogException(raw_log=raw_log)

        return Log(
            content=raw_log,
            response_time=response_time)