from vbench.api import GitRepo
from vbench.benchmark import gather_benchmarks
from datetime import datetime, timedelta

import os

modules = ['linear_model', 'cluster', 'semi_supervised', 'naive_bayes', 'svm',
           'decomposition', 'neighbors', 'covariance', 'gaussian_process',
           'mixture', 'pls']

by_module = {}
benchmarks = []
for mod in modules:
    by_module[mod] = [b for b in gather_benchmarks(__import__(mod).__dict__)]
    benchmarks.extend(by_module[mod])

for bm in benchmarks:
    assert(bm.name is not None)

import getpass
import sys

USERNAME = getpass.getuser()

# XXX: do we want platform independence here?
# I'm guessing the original supported MacOS because of the dev's laptop, and
# *nix because of the deployment server. Will we ever deploy this on IIS? :)

if sys.platform == 'darwin':
    HOME = '/Users/%s' % USERNAME
else:
    HOME = '/home/%s' % USERNAME

REPO_PATH = os.path.join(HOME, 'code/scikit-learn')
REPO_URL = 'git@github.com:scikit-learn/scikit-learn.git'
DB_PATH = os.path.join(HOME,
                       'code/scikit-learn-speed/benchmarks/benchmarks.db')
TMP_DIR = '/tmp/vb_sklearn'

PREPARE = """
python setup.py clean
"""
BUILD = """
python setup.py build_ext --inplace
"""
dependencies = ['deps.py', 'data']

# this is for debugging purposes, only run a couple of days of commits
START_DATE = datetime.now() - timedelta(days=6)
#START_DATE = datetime(2012, 1, 1)
repo = GitRepo(REPO_PATH)

RST_BASE = '../doc'


def generate_rst_files(benchmarks):
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt

    vb_path = os.path.join(RST_BASE, 'vbench')
    fig_base_path = os.path.join(vb_path, 'figures')

    def plot_benchmark(benchmark, column, label):
        fig_filename = '%s-%s.png' % (benchmark.name, column)

        # create paths
        fig_full_path = os.path.join(fig_base_path, fig_filename)
        fig_rel_path = 'vbench/figures/%s' % fig_filename

        # plot the figure
        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        benchmark.plot(DB_PATH, ax=ax, y=column, ylabel=label)

        start, end = ax.get_xlim()
        plt.xlim([start - 30, end + 30])
        plt.savefig(fig_full_path, bbox_inches='tight')
        plt.close('all')
        return fig_rel_path

    if not os.path.exists(vb_path):
        print 'creating %s' % vb_path
        os.makedirs(vb_path)

    if not os.path.exists(fig_base_path):
        print 'creating %s' % fig_base_path
        os.makedirs(fig_base_path)

    for bmk in benchmarks:
        print 'Generating rst file for %s' % bmk.name
        rst_path = os.path.join(RST_BASE, 'vbench/%s.txt' % bmk.name)
        image_paths = []  # tuple of (title, full_path, rel_path)

        # TODO: condition this as well. Maybe some benchmarks are only for mem
        image_paths.append(('Execution time',
                            plot_benchmark(bmk, 'timing', 'miliseconds')))

        if bmk.memory:
            image_paths.append(('Memory usage',
                                plot_benchmark(bmk, 'memory', 'megabytes')))

        rst_text = bmk.to_rst(image_paths)
        with open(rst_path, 'w') as f:
            f.write(rst_text)

    with open(os.path.join(RST_BASE, 'index.rst'), 'w') as f:
        print >> f, """
Performance Benchmarks
======================

These historical benchmark graphs were produced with `vbench
<http://github.com/pydata/vbench>`__.

Produced on a machine with TODO

.. toctree::
    :hidden:
    :maxdepth: 3
"""
        for modname, mod_bmks in sorted(by_module.items()):
            print >> f, '    vb_%s' % modname
            modpath = os.path.join(RST_BASE, 'vb_%s.rst' % modname)
            with open(modpath, 'w') as mh:
                header = '%s\n%s\n\n' % (modname, '=' * len(modname))
                print >> mh, header

                for bmk in mod_bmks:
                    print >> mh, bmk.name
                    print >> mh, '-' * len(bmk.name)
                    print >> mh, '.. include:: vbench/%s.txt\n' % bmk.name
