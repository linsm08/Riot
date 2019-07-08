# -*- coding: utf-8 -*-

import abc

class SourceProvider(object):
    @abc.abstractmethod
    def get_logs_iterator():
        pass