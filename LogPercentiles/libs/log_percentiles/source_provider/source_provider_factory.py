# -*- coding: utf-8 -*-

from LogPercentiles.libs.log_percentiles.source_provider.concrete_source_provider.log_directory_source_provider import LogDirectorySourceProvider
from LogPercentiles.libs.log_percentiles.source_provider.concrete_source_provider.memory_source_provider import MemorySourceProvider

class SourceProviderFactory(object):
    
    @classmethod
    def get_log_directory_provider(self, directory, raw_log_parser):
        return LogDirectorySourceProvider(directory, raw_log_parser)
        

    @classmethod
    def get_memory_provider(self, raw_logs, raw_log_parser):
        return MemorySourceProvider(raw_logs, raw_log_parser)
        