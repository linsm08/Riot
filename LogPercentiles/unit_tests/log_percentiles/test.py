# -*- coding: utf-8 -*-

from LogPercentiles.libs.log_percentiles.utility.log_percentile_calculator import LogPercentileCalculator
from LogPercentiles.libs.log_percentiles.source_provider.source_provider_factory import SourceProviderFactory
from LogPercentiles.libs.log_percentiles.source_provider.raw_log_parser.log_file_raw_log_parser import LogFileRawLogParser

def main():
    directory = "/home/antonylin/Code/projects/Riot/LogPercentiles/unit_tests/log_percentiles/data/log_directory1"
    log_provider = SourceProviderFactory.get_log_directory_provider(
        directory=directory,
        raw_log_parser=LogFileRawLogParser()
    )

    percentiles = [0.9, 0.95, 0.99]
    calculator = LogPercentileCalculator(percentiles=percentiles)
    calculator.run(provider=log_provider)

if __name__ == "__main__":
    main()