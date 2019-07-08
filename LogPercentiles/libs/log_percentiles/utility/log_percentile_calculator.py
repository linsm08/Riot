# -*- coding: utf-8 -*-

import math

class LogPercentileCalculator(object):
    def __init__(self, percentiles, result_comsumer=None):
        if not percentiles:
            raise ValueError("percentiles should not be None or empty.")
        if not isinstance(percentiles, list):
            raise ValueError("percentiles should be a list.")
        if any([p <= 0 or p > 1 for p in percentiles]):
            raise ValueError("Values in percentiles should between 0 and 1.")
        
        self._percentiles = percentiles
        self._result_comsumer = result_comsumer

    def run(self, provider):
        logs = provider.get_logs_iterator()
        response_times = []
        percentile_times = []

        for log in logs:
            response_times.append(log.response_time)

        total_count = len(response_times)
        if total_count:
            response_times.sort()
            indexes = [int(math.ceil(p * total_count)) for p in self._percentiles]
            indexes = [i if i < total_count else total_count - 1 for i in indexes]
            percentile_times = [response_times[i] for i in indexes]

        result = zip(self._percentiles, percentile_times)

        if self._result_comsumer:
            self._result_comsumer(result)

        return result

class LogPercentileComsumer(object):
    @staticmethod
    def print_result(percentile_times):
        for percentile_time in percentile_times:
            print "{0:.0%} of requests return a response within {1} ms".format(percentile_time[0], percentile_time[1])