Quick start
===========

Scikit-learn-speed is a continuous benchmarking suite that accompanies the 
`scikit-learn <http://www.scikit-learn.org/>`_ project. It is built on top of
`vbench <http://wesmckinney.com/blog/?p=373>`_.

Dependencies
------------

In order to run the benchmarks, you must have the following packages installed:

  - The development version of vbench from `Vlad's repository <https://github.com/vene/vbench/tree/abstract_benchmarks>`_.
  - `Numpy <http://numpy.scipy.org/>`_, `Scipy <http://scipy.org/>`_

Vbench itself requires:

  - `git <http://git-scm.com/>`_ (it should be in the path, old versions might fail)
  - `Pandas <http://pandas.pydata.org/>`_ (and its dependencies)
  - `sqlalchemy <http://www.sqlalchemy.org/>`_
  - `memory_profiler <http://pypi.python.org/pypi/memory_profiler>`_ (optional, for memory usage benchmarking)

For building the web pages (that you are looking at right now), you
additionally need:

  - `Sphinx <http://sphinx.pocoo.org/>`_
  - `Matplotlib <http://matplotlib.sourceforge.net/>`_


Installation
------------

Just fetch the latest code from the `Github repository <https://github.com/vene/scikit-learn-speed/>`_.

Running the benchmarks
----------------------

In order to run the benchmarks on your own machine, you need to:

1. Clone the repository somewhere, for example ``~/code/scikit-learn-speed``

2. Extract the datasets::

    cd ~/code/scikit-learn-speed/benchmarks
    tar jxvf data.tar.bz2


3. Create the configuration file ``~/.vbench-skl``. For example::

    [setup]
    repo_path = /Users/vene/code/scikit-learn
    repo_url = git@github.com:scikit-learn/scikit-learn.git
    db_path = /Users/vene/code/scikit-learn-speed/benchmarks/benchmarks.db
    tmp_dir = /tmp/vb_sklearn


The values displayed above are hardcoded defaults, and they are used in case
the configuration value doesn't exist, or to override skipped values.
Specifically, this means you don't have to bother to set ``repo_url`` and
``tmp_dir``.


4. From the ``scikit-learn-speed/benchmarks`` folder, run::

    python run_suite.py


You will now have a file called ``benchmarks.db`` in the ``benchmarks`` folder.
You can look inside this file using ``sqlite3`` or (recommended) by
instanciating a ``vbench.db.BenchmarksDB`` object, like this:

.. code-block:: python

	In [1]: from vbench.db import BenchmarkDB

	In [2]: db = BenchmarkDB('benchmarks/benchmarks.db')

	In [3]: db.get_benchmarks()
	Out[3]: 
	                                                                           name description
	checksum                                                                                   
	0ff90bcf3a75abe21cede6ede6674aba               LinearRegression-minimadelon-fit        None
	1b296252fc235e4b6d1559013263074e           LinearRegression-minimadelon-predict        None
	(...)

	In [4]: db.get_benchmark_results('0ff90bcf3a75abe21cede6ede6674aba')
	Out[4]: 
	                    revision ncalls    timing  timing_min  timing_max  timing_mean  timing_median  timing_std                                          profile    memory traceback
	timestamp                                                                                                                                                                           
	2012-07-23 14:07:14  6aaf15f   None  0.003620    0.001490    0.001876     0.001627       0.001515    0.000176           78 function calls in 0.004 seconds   O  0.121094      None
	2012-07-24 12:19:11  af2602e   None  0.002806    0.001489    0.001892     0.001670       0.001630    0.000167           78 function calls in 0.003 seconds   O  0.121094      None


Generating the documentation
----------------------------

To actually generate the HTML files, navigate to the ``scikit-learn-speed``
folder and execute::

    python make.py


You can view the results by opening
``scikit-learn-speed/benchmarks/build/html/index.html`` in your favourite
internet browser. An internet connection is recommended, because JQuery and
JQueryUI are loaded from Google's CDN.
