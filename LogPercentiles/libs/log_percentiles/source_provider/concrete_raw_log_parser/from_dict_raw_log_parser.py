# -*- coding: utf-8 -*-

from LogPercentiles.libs.log_percentiles.common.log import Log
from LogPercentiles.libs.log_percentiles.common.exception import InvalidRawLogException
from LogPercentiles.libs.log_percentiles.source_provider.base_raw_log_parser import RawLogParser

class FromDictRawLogParser(RawLogParser):
    '''
    Parse log from dictionary.
    Key response_time is required in dictionary.
    '''
    def build_log(self, raw_log):
        response_time = raw_log.get("response_time")
        if not response_time:
            raise InvalidRawLogException("raw_log should have response_time key.")
        if not isinstance(response_time, (int, long, float)):
            raise InvalidRawLogException("response_time should be number.")

        return Log(
            content=raw_log.get("content"),
            response_time=response_time
        )