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
    'predict': 'obj.predict(X_t)',
    'transform': 'obj.transform(X)',
    'fit_transform': 'obj.fit_transform(X)'
}

_setup_extra = {
    'fit': '',
    'predict': _statements['fit'],
    'transform': _statements['fit'],
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


def make_suite(config_arg_list, module):
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
