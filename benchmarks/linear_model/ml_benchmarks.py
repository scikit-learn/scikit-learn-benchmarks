from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'LassoLars',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'Lasso',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'ElasticNet',
     'init_params': {'rho': 0.5, 'alpha': 0.5},  # normalize here?
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(config_arg_list=_benchmarks, module='linear_model')
