# -*- coding: utf-8 -*-

import abc

class RawLogParser(object):
    @abc.abstractmethod
    def build_log(self):
        pass