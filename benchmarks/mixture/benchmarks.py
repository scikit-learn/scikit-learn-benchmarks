from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'DPGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict')
    },
    {
     'obj': 'GMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict')
    },
    {
     'obj': 'VBGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full'},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict')
    }
]

suite = _make_suite(_benchmarks)
