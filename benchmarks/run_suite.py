import sys

from vbench.api import BenchmarkRunner
from suite import *


if __name__ == '__main__':
    run_option = 30 if 'historical' in sys.argv else 'last'
    quick = 'quick' in sys.argv

    benchmarks, _ = gather(quick=quick)

    runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL,
                             BUILD, DB_PATH, TMP_DIR, PREPARE,
                             run_option=run_option, start_date=START_DATE,
                             module_dependencies=dependencies)
    runner.run()
