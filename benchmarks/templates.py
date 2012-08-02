from itertools import product

from vbench.benchmark import BenchmarkSuite, PythonBenchmark, \
                             LineProfilerBenchmarkMixin, \
                             CProfileBenchmarkMixin, MemoryBenchmarkMixin


class SklBenchmark(LineProfilerBenchmarkMixin, CProfileBenchmarkMixin,
                   MemoryBenchmarkMixin, PythonBenchmark):
    def __init__(self, *args, **kwargs):
        super(SklBenchmark, self).__init__(*args, **kwargs)
        if 'functions' not in kwargs:
            # Unreadable hack to get function name:
            import re
            self.functions = ['.'.join((
                          re.findall('from .+ import (.+)', self.setup)[0],
                          self.code.split('.')[1].split('(')[0]))]

    def plot(self, db_path, label='time', ax=None, title=True, y='timing',
             ylabel='seconds'):
        import matplotlib.pyplot as plt
        from matplotlib.dates import MonthLocator, DateFormatter

        results = self.get_results(db_path)

        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)

        if y == 'timing':
            timing = results['timing_min']
            std = results['timing_std']

            if self.start_date is not None:
                timing = timing.truncate(before=self.start_date)
                std = std.truncate(before=self.start_date)
            timing.plot(ax=ax, style='b-', label=label)
            (timing + std).plot(ax=ax, style='b:')
            (timing - std).plot(ax=ax, style='b:')
        else:
            timing = results[y]
            if self.start_date is not None:
                timing = timing.truncate(before=self.start_date)

            timing.plot(ax=ax, style='b-', label=label)

        ax.set_xlabel('Date')
        ax.set_ylabel(ylabel)

        if self.logy:
            ax2 = ax.twinx()
            try:
                timing.plot(ax=ax2, label='%s (log scale)' % label,
                            style='r-',
                            logy=self.logy)
                ax2.set_ylabel(ylabel + ' (log scale)')
                ax.legend(loc='best')
                ax2.legend(loc='best')
            except ValueError:
                pass

        ylo, yhi = ax.get_ylim()

        if ylo < 1:
            ax.set_ylim([0, yhi])

        formatter = DateFormatter("%b %Y")
        ax.xaxis.set_major_locator(MonthLocator())
        ax.xaxis.set_major_formatter(formatter)
        ax.autoscale_view(scalex=True)

        if title:
            ax.set_title(self.name)

        return ax

    def to_rst(self, db_path=None, image_paths=None):
        def indent(string, spaces=4):
            dent = ' ' * spaces
            return '\n'.join([dent + x for x in string.split('\n')])
        result = PythonBenchmark.to_rst(self, image_paths)

        if db_path:
            result += """\

**Additional output**

.. container:: profiler-output

"""

            results = self.get_results(db_path)
            for title, column in (('Traceback', 'traceback'),
                                  ('cProfile', 'profile'),
                                  ('LineProfiler', 'line_profile')):
                try:
                    out = results.get(column, [None])
                    out = out[-1]
                    if out:
                        result += indent("""\
.. container::

%s

::

""" % title, spaces=3) + indent(out, spaces=7)
                except IndexError:
                    pass
        return result

_setup = """
from sklearn.%(module)s import %(obj)s
from deps import load_data

kwargs = %(init_params)s
X, y, X_t, y_t = load_data('%(data)s')
obj = %(obj)s(**kwargs)
"""

_statements = {
    'fit': 'obj.fit(X, y)',
    'fit_unsup': 'obj.fit(X)',
    'predict': 'obj.predict(X_t)',
    'predict_unsup': 'obj.predict(X_t)',
    'transform': 'obj.transform(X)',
    'transform_unsup': 'obj.transform(X)',
    'fit_transform': 'obj.fit_transform(X)'
}

_setup_extra = {
    'fit': '',
    'fit_unsup': '',
    'predict': _statements['fit'],
    'transform': _statements['fit'],
    'predict_unsup': _statements['fit_unsup'],
    'transform_unsup': _statements['fit_unsup'],
    'fit_transform': ''
}


def join_safe(terms, joiner='-'):
    """Joins the terms like str.join but skipping Nones

    Example:
      >> terms = 'Mary', 'had', None, 'fun'
      >> ' '.join(terms)
      "Mary had  fun"
      >> join_safe(('Mary', 'had', None, 'fun'), ' ')
      "Mary had fun"

    """
    return '-'.join(filter(lambda x: x is not None, terms))


def make_suite(config_arg_list, module=None):
    if module is None:
        try:
            # Do some tricks to automatically guess module name
            # just for some extra sugar in the benchmark file
            import inspect
            frm = inspect.stack()[1]
            module = inspect.getmodule(frm[0]).__name__
            module = module.split('.')[0]
        except:
            raise ValueError('Unable to guess module name. Please specify it '
                             'manually in the benchmarks file.')
    configs = [
        (
            join_safe((arg['obj'], arg.get('spec'), data, stmt)),  # name
            _statements[stmt],                      # statement to bench
            _setup % {                              # setup
                'obj': arg['obj'],
                'init_params': str(arg['init_params']),
                'data': data,
                'module': module
            } + _setup_extra[stmt]
        )
        for arg in config_arg_list
        for data, stmt in product(arg['datasets'], arg['statements'])
    ]

    return BenchmarkSuite(SklBenchmark(code, setup, name=name)
                          for name, code, setup in configs)
