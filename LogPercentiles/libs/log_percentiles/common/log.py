# -*- coding: utf-8 -*-

class Log(object):
    def __init__(self, content, response_time):
        self._response_time = response_time
        self._content = content

    @property
    def response_time(self):
        # make response_time readonly
        return self._response_time

    @property
    def content(self):
        # make content readonly
        return self._content