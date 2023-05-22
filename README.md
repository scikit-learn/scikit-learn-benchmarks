![.github/workflows/check_last_run.yml](https://github.com/scikit-learn/scikit-learn-benchmarks/workflows/Last%20run/badge.svg)

# scikit-learn-benchmarks

The results of scikit-learn asv benchmarks are automatically published every day on the following dashboard:

https://scikit-learn.org/scikit-learn-benchmarks/

### Major changes

- May 22nd 2023: switch from conda default channel to conda-forge; upgrade Python version from 3.8 to latest. A consequence is that for these benchmarks Scikit-learn now uses OpenBLAS (previously MKL) which explains the discrpency in the timeline.
