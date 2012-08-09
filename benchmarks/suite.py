import os
import getpass
import sys
from datetime import datetime, timedelta

from vbench.api import GitRepo
from vbench.benchmark import gather_benchmarks

###################
# Gather benchmarks


def gather(quick=False):
    modules = ['linear_model'] if quick else \
              ['linear_model', 'cluster', 'semi_supervised', 'naive_bayes',
               'svm', 'decomposition', 'neighbors', 'covariance', 'manifold',
               'gaussian_process', 'mixture', 'pls', 'tree', 'ensemble']

    by_module = {}
    benchmarks = []
    for mod in modules:
        by_module[mod] = [b for b in gather_benchmarks(
                                                    __import__(mod).__dict__)]
        benchmarks.extend(by_module[mod])

    return benchmarks, by_module

###############
# Configuration

USERNAME = getpass.getuser()

# XXX: do we want platform independence here?
# I'm guessing the original supported MacOS because of the dev's laptop, and
# *nix because of the deployment server. Will we ever deploy this on IIS? :)

if sys.platform == 'darwin':
    HOME = '/Users/%s' % USERNAME
else:
    HOME = '/home/%s' % USERNAME

# Configuration defaults

REPO_PATH = os.path.join(HOME, 'code/scikit-learn')
REPO_URL = 'git@github.com:scikit-learn/scikit-learn.git'
DB_PATH = os.path.join(HOME,
                       'code/scikit-learn-speed/benchmarks/benchmarks.db')
TMP_DIR = '/tmp/vb_sklearn'

try:
    import ConfigParser

    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.expanduser('~/.vbench-skl')))

    def get_config(key, var):
        if config.has_option('setup', key):
            return config.get('setup', key)
        else:
            print "The %s option is not set. Reverting to default." % key
            return var

    REPO_PATH = get_config('repo_path', REPO_PATH)
    REPO_URL = get_config('repo_url', REPO_URL)
    DB_PATH = get_config('db_path', DB_PATH)
    TMP_DIR = get_config('tmp_dir', TMP_DIR)
except:
    print "Cannot load configuration file. Reverting to defaults."

PREPARE = """
python setup.py clean
"""
BUILD = """
python setup.py build_ext --inplace
"""

RST_BASE = 'doc'

dependencies = ['benchmarks/deps.py', 'benchmarks/templates.py',
                'benchmarks/data']

START_DATE = datetime.now() - timedelta(days=400)
repo = GitRepo(REPO_PATH)


# Helper function, move it?
def generate_rst_files(benchmarks, by_module):
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt

    vb_path = os.path.join(RST_BASE, 'vbench')
    fig_base_path = os.path.join(vb_path, 'figures')

    def plot_benchmark(benchmark, step_no, column, label):
        fig_filename = '%s-step%d-%s.png' % (benchmark.name, step_no, column)

        # create paths
        fig_full_path = os.path.join(fig_base_path, fig_filename)
        fig_rel_path = 'vbench/figures/%s' % fig_filename

        # plot the figure
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        benchmark.plot(DB_PATH, ax=ax, y=column, ylabel=label, step_no=step_no)
        ylo, yhi = ax.get_ylim()
        plt.ylim([0.0, 1.1 * yhi])
        start, end = ax.get_xlim()
        plt.xlim([start - 30, end + 30])
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(66)

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
        image_paths = []
        for step_no in xrange(len(bmk.code)):
            image_path = []  # tuple of (title, full_path, rel_path)
            # TODO: condition this as well. Maybe some benchmarks are only mem
            image_path.append(('Execution time', plot_benchmark(bmk, step_no,
                                                        'timing', 'seconds')))

            image_path.append(('Memory usage', plot_benchmark(bmk, step_no,
                                                      'memory', 'megabytes')))
            image_paths.append(image_path)

        rst_text = bmk.to_rst(DB_PATH, image_paths)
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
                modname = 'Benchmarks for ' + modname
                header = '%s\n%s\n\n' % (modname, '=' * len(modname))
                print >> mh, header

                for bmk in mod_bmks:
                    print >> mh, '.. include:: vbench/%s.txt\n' % bmk.name
