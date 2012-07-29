import sys

from suite import generate_rst_files, gather

if __name__ == '__main__':
    quick = 'quick' in sys.argv
    benchmarks, by_module = gather(quick=quick)
    generate_rst_files(benchmarks, by_module)
