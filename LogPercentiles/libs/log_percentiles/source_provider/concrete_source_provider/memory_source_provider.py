# -*- coding: utf-8 -*-

import os
from LogPercentiles.libs.log_percentiles.common.exception import InvalidRawLogException
from LogPercentiles.libs.log_percentiles.source_provider.base_source_provider import SourceProvider

class MemorySourceProvider(SourceProvider):
    '''
    Iterate source from memory.
    '''
    def __init__(self, raw_logs, raw_log_parser):
        self._raw_logs = raw_logs
        self._raw_log_parser = raw_log_parser

        if self._raw_logs is None:
            raise ValueError("director should not be None or Empty.")
        if not self._raw_log_parser:
            raise ValueError("raw_log_parser should not be None.")

    def get_logs_iterator(self):
        for raw_log in self._raw_logs:
            yield self._raw_log_parser.build_log(raw_log)