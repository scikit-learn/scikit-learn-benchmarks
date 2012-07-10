from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'DPGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'GMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'VBGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit', 'predict')
    }
]

suite = _make_suite(_benchmarks)
