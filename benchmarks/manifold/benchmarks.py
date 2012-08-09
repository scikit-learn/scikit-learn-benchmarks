from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'Isomap',
     'spec': 'dense',
     'init_params': {'solver': 'dense'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'Isomap',
     'spec': 'arpack',
     'init_params': {'solver': 'arpack'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'arpack',
     'init_params': {'solver': 'arpack', 'method': 'standard',
                     'random_state': 0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'arpack',
     'init_params': {'solver': 'arpack', 'method': 'hessian',
                     'random_state': 0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'arpack',
     'init_params': {'solver': 'arpack', 'method': 'modified',
                     'random_state': 0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'LocallyLinearEmbedding',
     'spec': 'arpack',
     'init_params': {'solver': 'arpack', 'method': 'ltsa'},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    },
    {
     'obj': 'MDS',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'transform_unsup')
    }
]


suite = _make_suite(_benchmarks)
