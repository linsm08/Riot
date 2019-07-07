# -*- coding: utf-8 -*-

from LogPercentiles.libs.log_percentiles.source_provider.log_directory_source_provider import LogDirectorySourceProvider

class SourceProviderFactory(object):
    
    @classmethod
    def get_log_directory_provider(self, directory, raw_log_parser):
        return LogDirectorySourceProvider(directory, raw_log_parser)
        