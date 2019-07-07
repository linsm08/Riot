# -*- coding: utf-8 -*-

class LogPercentileCalculator(object):
    def __init__(self, percentiles):
        if not percentiles:
            raise ValueError("percentiles should not be None or empty.")
        if not isinstance(percentiles, list):
            raise ValueError("percentiles should be a list.")
        
        self._percentiles = percentiles

    def run(self, provider):
        logs = provider.get_logs_iterator()
        for log in logs:
            print log.response_time
            pass