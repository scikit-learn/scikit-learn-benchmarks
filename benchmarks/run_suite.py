import sys

from vbench.api import BenchmarkRunner
from suite import *


def run_process(run_option):
    runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL,
                             BUILD, DB_PATH, TMP_DIR, PREPARE,
                             run_option=run_option, start_date=START_DATE,
                             module_dependencies=dependencies)
    runner.run()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'releases':
        from datetime import datetime
        run_option = [
            datetime(year=2012, month=5, day=8),  # 0.11
            datetime(year=2012, month=1, day=11),  # 0.10
            datetime(year=2011, month=12, day=20),  # 0.9
            datetime(year=2011, month=5, day=25),  # 0.8.1
            datetime(year=2011, month=3, day=9),  # 0.7.1
        ]
    else:
        run_option = 'last'
    run_process(run_option)
