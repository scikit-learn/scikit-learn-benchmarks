from vbench.api import Benchmark, GitRepo
from datetime import datetime, timedelta

import os

modules = ['linear_model']

by_module = {}
benchmarks = []

for modname in modules:
    ref = __import__(modname)
    by_module[modname] = [v for v in ref.__dict__.values()
                          if isinstance(v, Benchmark)]
    benchmarks.extend(by_module[modname])

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
dependencies = ['deps.py']

# this is for debugging purposes, only run a couple of days of commits
START_DATE = datetime.now() - timedelta(days=3)

repo = GitRepo(REPO_PATH)

RST_BASE = '../doc'


def generate_rst_files(benchmarks):
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt

    vb_path = os.path.join(RST_BASE, 'vbench')
    fig_base_path = os.path.join(vb_path, 'figures')

    if not os.path.exists(vb_path):
        print 'creating %s' % vb_path
        os.makedirs(vb_path)

    if not os.path.exists(fig_base_path):
        print 'creating %s' % fig_base_path
        os.makedirs(fig_base_path)

    for bmk in benchmarks:
        print 'Generating rst file for %s' % bmk.name
        rst_path = os.path.join(RST_BASE, 'vbench/%s.txt' % bmk.name)

        fig_full_path = os.path.join(fig_base_path, '%s.png' % bmk.name)

        # make the figure
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        bmk.plot(DB_PATH, ax=ax)

        start, end = ax.get_xlim()

        plt.xlim([start - 30, end + 30])
        plt.savefig(fig_full_path, bbox_inches='tight')
        plt.close('all')

        fig_rel_path = 'vbench/figures/%s.png' % bmk.name
        rst_text = bmk.to_rst(image_path=fig_rel_path)
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
