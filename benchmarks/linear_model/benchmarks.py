from templates import make_suite as _make_suite

_benchmarks = [
    #{
    # 'obj': 'LinearRegression',
    # 'init_params': {},
    # 'datasets': ('madelon',),
    # 'statements': ('fit',)
    #},
    {
     'obj': 'Ridge',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'Lars',
     'init_params': {'normalize': False},
     'datasets': ('minimadelon-oney', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'LassoLars',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('minimadelon-oney', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'Lasso',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('minimadelon-oney', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'ElasticNet',
     'init_params': {'rho': 0.5, 'alpha': 0.5},  # normalize here?
     'datasets': ('minimadelon-oney',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'OrthogonalMatchingPursuit',
     'init_params': {'n_nonzero_coefs': 10},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'SGDClassifier',
     'init_params': {},
     'datasets': ('madelon', 'newsgroups'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LogisticRegression',
     'init_params': {'C': 1e5},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'ARDRegression',
     'init_params': {},
     'datasets': ('minimadelon-oney', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'BayesianRidge',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    }
]

suite = _make_suite(config_arg_list=_benchmarks)
