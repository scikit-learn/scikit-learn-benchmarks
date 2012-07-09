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
     'init_params': {'n_components': 9},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'ProbabilisticPCA',
     'init_params': {'n_components': 9},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'KernelPCA',
     'init_params': {'n_components': 9, 'kernel': 'rbf'},
     'spec': 'rbf',
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'KernelPCA',
     'init_params': {'n_components': 9, 'kernel': 'sigmoid'},
     'spec': 'sigmoid',
     'datasets': ('arcene', 'madelon'),
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
    {
     'obj': 'MiniBatchDictionaryLearning',
     'init_params': {'n_components': 100},
     'datasets': ('arcene',),
     'statements': ('fit', 'transform', 'fit_transform')
    },
    {
     'obj': 'MiniBatchSparsePCA',
     'init_params': {'n_components': 2},
     'datasets': ('madelon',),
     'statements': ('fit', 'transform', 'fit_transform')
    },
]

suite = _make_suite(config_arg_list=_benchmarks, module='decomposition')
