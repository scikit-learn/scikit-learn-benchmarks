scikit-learn-speed
==================

Continuous benchmark suite for the scikit-learn project. For more information,
check out http://vene.github.com/scikit-learn-speed

Usage
-----

In order to run the benchmarks on your own machine, please follow these steps.

1. Clone the repository somewhere, for example ``~/code/scikit-learn-speed``

2. Extract the datasets:
    ```
    cd ~/code/scikit-learn-speed/benchmarks
    tar jxvf data.tar.bz2
    ```

3. Create the configuration file ``~/.vbench-skl``. For example:
    ```
    [setup]
    repo_path = /Users/vene/code/scikit-learn
    repo_url = git@github.com:scikit-learn/scikit-learn.git
    db_path = /Users/vene/code/scikit-learn-speed/benchmarks/benchmarks.db
    tmp_dir = /tmp/vb_sklearn
    ```


The values displayed above are hardcoded defaults, and they are used in case
the configuration value doesn't exist, or to override skipped values.
Specifically, this means you don't have to bother to set ``repo_url`` and
``tmp_dir``.

4. From the ``scikit-learn-speed`` folder run ``make``. This will call:

 - ``make run``, which runs the benchmark suite,
 - ``make rst``, which generates the Sphinx sources for the reports,
 - ``make html``, which builds the HTML reports from the sources.

For more details see ``make help``. 

6. You can view the results by opening
``scikit-learn-speed/benchmarks/build/html/index.html``.


Datasets
--------

The following datasets are available:

- arcene: train: (100, 10000), test: (100, 10000)
- madelon: train: (2000, 500), test: (600, 500)
- minimadelon: train: (30, 500), test: (20, 500), 10 output
- blobs: train: (300, 50) test: (200, 50), 10 tight centers
- newsgroups: sparse, train: (11214, 130088), test: (7432, 130088)

In addition, you can append the following options to any dataset's name:

- `-oney`: Only keeps the first output, i. e. `y = y[:, 0]`. Necessary
for estimators that don't support multidimensional output arrays.
- `-semi`: Unlabels samples at random, by setting the corresponding output
to `-1`. Useful for semi-supervised algorithms.

