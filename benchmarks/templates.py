from itertools import product

from vbench.benchmark import Benchmark, BenchmarkSuite

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
    'transform': 'obj.transform(X)',
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

    return BenchmarkSuite(Benchmark(code, setup, name=name, memory=True)
                          for name, code, setup in configs)
