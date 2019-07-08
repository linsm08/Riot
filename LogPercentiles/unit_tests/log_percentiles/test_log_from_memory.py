# -*- coding: utf-8 -*-

import unittest

from LogPercentiles.libs.log_percentiles.common.exception import InvalidRawLogException
from LogPercentiles.libs.log_percentiles.utility.log_percentile_calculator import LogPercentileCalculator, LogPercentileComsumer
from LogPercentiles.libs.log_percentiles.source_provider.source_provider_factory import SourceProviderFactory
from LogPercentiles.libs.log_percentiles.source_provider.concrete_raw_log_parser.from_dict_raw_log_parser import FromDictRawLogParser

class TestLogFromMemory(unittest.TestCase):
    def test_success(self):
        # Valid log source. At least one log input.
        log_provider = SourceProviderFactory.get_memory_provider(
            raw_logs=[{"response_time": 1000 + i} for i in xrange(1000)],
            raw_log_parser=FromDictRawLogParser()
        )

        percentiles = [0.01, 0.5, 0.6, 0.95, 0.99]
        calculator = LogPercentileCalculator(
            percentiles=percentiles,
            result_comsumer=LogPercentileComsumer.print_result)
        result = calculator.run(provider=log_provider)

        expected_result = zip(percentiles, [1010, 1500, 1600, 1950, 1990])
        self.assertEqual(result, expected_result)


    def test_success_empty_log_source(self):
        # Empty log input.
        log_provider = SourceProviderFactory.get_memory_provider(
            raw_logs=[], # Empty log input here.
            raw_log_parser=FromDictRawLogParser()
        )

        percentiles = [0.01, 0.5, 0.6, 0.95, 0.99]
        calculator = LogPercentileCalculator(
            percentiles=percentiles,
            result_comsumer=LogPercentileComsumer.print_result)
        result = calculator.run(provider=log_provider)

        expected_result = zip(percentiles, [])
        self.assertEqual(result, expected_result)


    def test_success_log_number_less_than_percentiles(self):
        # Valid log source. But the number of log is less than the number of percentiles.
        log_provider = SourceProviderFactory.get_memory_provider(
            raw_logs=[{"response_time": 1000 + i} for i in xrange(2)], # Only 2 logs from source.
            raw_log_parser=FromDictRawLogParser()
        )

        percentiles = [0.01, 0.5, 0.6, 0.95, 0.99]
        calculator = LogPercentileCalculator(
            percentiles=percentiles,
            result_comsumer=LogPercentileComsumer.print_result)
        result = calculator.run(provider=log_provider)

        expected_result = zip(percentiles, [1001, 1001, 1001, 1001, 1001])
        self.assertEqual(result, expected_result)


    def test_failed_invalid_percentiles(self):
        log_provider = SourceProviderFactory.get_memory_provider(
            raw_logs=[{"response_time": 1000 + i} for i in xrange(2)], # Only 2 logs from source.
            raw_log_parser=FromDictRawLogParser()
        )

        with self.assertRaises(ValueError):
            percentiles = [0, 0.99]
            calculator = LogPercentileCalculator(
                percentiles=percentiles,
                result_comsumer=LogPercentileComsumer.print_result)
            calculator.run(provider=log_provider)

        with self.assertRaises(ValueError):
            percentiles = [0.1, 1.1]
            calculator = LogPercentileCalculator(
                percentiles=percentiles,
                result_comsumer=LogPercentileComsumer.print_result)
            calculator.run(provider=log_provider)


    def test_failed_invalid_raw_log(self):
        # Input log is invalid for no response_time in raw_log.
        log_provider = SourceProviderFactory.get_memory_provider(
            raw_logs=[{} for i in xrange(1000)],
            raw_log_parser=FromDictRawLogParser()
        )

        with self.assertRaises(InvalidRawLogException):
            # Assert that InvalidRawLogException is raised
            percentiles = [0.01, 0.5, 0.6, 0.95, 0.99]
            calculator = LogPercentileCalculator(
                percentiles=percentiles,
                result_comsumer=LogPercentileComsumer.print_result)
            calculator.run(provider=log_provider)


if __name__ == "__main__":
    unittest.main()
