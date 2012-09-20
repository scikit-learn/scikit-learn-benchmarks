from templates import make_suite as _make_suite

_benchmarks = [
#    {
#     'obj': 'PCA',
#     'init_params': {'n_components': 9},
#     'datasets': ('arcene', 'madelon'),
#     'statements': ('fit', 'transform', 'fit_transform')
#    },
    {
     'obj': 'RandomizedPCA',
     'init_params': {'n_components': 9, 'random_state': 0},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit_unsup', 'fit_transform')
    },
    {
     'obj': 'ProbabilisticPCA',
     'init_params': {'n_components': 9},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup', 'fit_transform')
    },
    {
     'obj': 'KernelPCA',
     'init_params': {'n_components': 9, 'kernel': 'rbf'},
     'spec': 'rbf',
     'datasets': ('minimadelon',),
     'statements': ('fit_unsup', 'transform_unsup', 'fit_transform')
    },
    {
     'obj': 'KernelPCA',
     'init_params': {'n_components': 9, 'kernel': 'sigmoid'},
     'spec': 'sigmoid',
     'datasets': ('minimadelon',),
     'statements': ('fit_unsup', 'transform_unsup', 'fit_transform')
    },
    {
     'obj': 'FastICA',
     'spec': 'deflation',
     'init_params': {'n_components': 9, 'algorithm': 'deflation',
                     'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'FastICA',
     'spec': 'parallel',
     'init_params': {'n_components': 9, 'algorithm': 'parallel',
                     'random_state': 0},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'NMF',
     'init_params': {'n_components': 2, 'init': 'nndsvd'},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'transform_unsup', 'fit_transform')
    },
    {
     'obj': 'MiniBatchDictionaryLearning',
     'init_params': {'n_atoms': 50, 'n_iter': 300, 'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'transform_unsup', 'fit_transform')
    },
    {
     'obj': 'MiniBatchSparsePCA',
     'init_params': {'n_components': 2, 'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'fit_transform')
    },
]

suite = _make_suite(_benchmarks)
