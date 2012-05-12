#!/usr/bin/env python

"""
Python script for building the vbench suite.

Usage
-----
python make.py clean
python make.py html
"""

import os
import shutil
import sys

os.environ['PYTHONPATH'] = '..'

SPHINX_BUILD = 'sphinxbuild'


def clean():
    if os.path.exists('benchmarks/build'):
        shutil.rmtree('benchmarks/build')

    if os.path.exists('doc/generated'):
        shutil.rmtree('doc/generated')


def html():
    check_build()
    if os.system('sphinx-build -P -b html -d benchmarks/build/doctrees '
                 'doc benchmarks/build/html'):
        raise SystemExit("Building HTML failed.")


def latex():
    check_build()
    if sys.platform != 'win32':
        # LaTeX format.
        if os.system('sphinx-build -b latex -d benchmarks/build/doctrees '
                     'source benchmarks/build/latex'):
            raise SystemExit("Building LaTeX failed.")
        # Produce pdf.

        os.chdir('benchmarks/build/latex')

        # Call the makefile produced by sphinx...
        if os.system('make'):
            raise SystemExit("Rendering LaTeX failed.")

        os.chdir('../..')
    else:
        print 'latex build has not been tested on windows'


def check_build():
    build_dirs = [
        'benchmarks/build', 'benchmarks/build/doctrees',
        'benchmarks/build/html', 'benchmarks/build/latex',
        'benchmarks/build/plots', 'benchmarks/build/_static',
        'benchmarks/build/_templates']
    for d in build_dirs:
        try:
            os.mkdir(d)
        except OSError:
            pass


def all_():
    # clean()
    html()

funcd = {
    'html':         html,
    'latex':        latex,
    'clean':        clean,
    'all':          all_,
    }

small_docs = False

# current_dir = os.getcwd()
# os.chdir(os.path.dirname(os.path.join(current_dir, __file__)))

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        func = funcd.get(arg)
        if func is None:
            raise SystemExit('Do not know how to handle %s; valid args are %s'
                             % (arg, funcd.keys()))
        func()
else:
    small_docs = False
    all_()
