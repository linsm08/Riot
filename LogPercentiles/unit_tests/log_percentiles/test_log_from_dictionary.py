# -*- coding: utf-8 -*-

import unittest

from LogPercentiles.libs.log_percentiles.utility.log_percentile_calculator import LogPercentileCalculator, LogPercentileComsumer
from LogPercentiles.libs.log_percentiles.source_provider.source_provider_factory import SourceProviderFactory
from LogPercentiles.libs.log_percentiles.source_provider.concrete_raw_log_parser.log_file_raw_log_parser import LogFileRawLogParser

class TestLogFromDirectory(unittest.TestCase):
    def test_success(self):
        directory = "/home/antonylin/Code/projects/Riot/LogPercentiles/unit_tests/log_percentiles/data/log_directory1"
        log_provider = SourceProviderFactory.get_log_directory_provider(
            directory=directory,
            raw_log_parser=LogFileRawLogParser()
        )

        percentiles = [0.01, 0.95, 0.99]
        calculator = LogPercentileCalculator(
            percentiles=percentiles,
            result_comsumer=LogPercentileComsumer.print_result)
        result = calculator.run(provider=log_provider)
        expected_result = zip(percentiles, [1002, 1190, 1198])
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
