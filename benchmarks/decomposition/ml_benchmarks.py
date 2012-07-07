from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'PCA',
     'init_params': {'n_components': 9},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'RandomizedPCA',
     'init_params': str({'n_components': 9}),
     'datasets': ('arcene', 'madelon', 'newsgroups'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'FastICA',
     'spec': 'deflation',
     'init_params': {'n_components': 9, 'algorithm': 'deflation'},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'FastICA',
     'spec': 'parallel',
     'init_params': {'n_components': 9, 'algorithm': 'parallel'},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'NMF',
     'init_params': {'n_components': 2},
     'datasets': ('blobs',),
     'statements': ('fit', 'transform', 'fit_transform')
    },
]

suite = _make_suite(config_arg_list=_benchmarks, module='decomposition')
