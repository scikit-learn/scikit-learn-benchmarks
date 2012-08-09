from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'Isomap',
     'spec': 'dense',
     'init_params': {'eigen_solver': 'dense'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'Isomap',
     'spec': 'arpack',
     'init_params': {'eigen_solver': 'arpack'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'standard',
     'init_params': {'eigen_solver': 'arpack', 'method': 'standard',
                     'random_state': 0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'hessian',
     'init_params': {'eigen_solver': 'arpack', 'method': 'hessian',
                     'random_state': 0, 'n_neighbors': 6},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'modified',
     'init_params': {'eigen_solver': 'arpack', 'method': 'modified',
                     'random_state': 0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'ltsa',
     'init_params': {'eigen_solver': 'arpack', 'method': 'ltsa'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    #
    #{
    # 'obj': 'MDS',
    # 'init_params': {},
    # 'datasets': ('minimadelon', 'blobs'),
    # 'statements': ('fit_unsup',)
    #}
]


suite = _make_suite(_benchmarks)
