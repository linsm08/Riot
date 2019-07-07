# -*- coding: utf-8 -*-

import os
from LogPercentiles.libs.log_percentiles.common.exception import InvalidRawLogException
from LogPercentiles.libs.log_percentiles.source_provider.source_provider import SourceProvider

class LogDirectorySourceProvider(SourceProvider):
    '''
    Iterate log files from director specified.
    Files in sub directory are ignored.
    '''
    def __init__(self, director, raw_log_parser):
        self._director = director
        self._raw_log_parser = raw_log_parser

        if not self._director:
            raise ValueError("director should not be None or Empty.")
        if not self._raw_log_parser:
            raise ValueError("raw_log_parser should not be None.")

    def get_logs_iterator(self):
        for filename in os.listdir(self._director):
            full_filename = os.path.join(self._director, filename)
            if os.path.isfile(full_filename):
                with open(full_filename, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        try:
                            log = self._raw_log_parser.build_log(line)
                        except InvalidRawLogException as ex:
                            # log here in product release
                            continue
                        yield log
