from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'DPGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full',
                     'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict_unsup')
    },
    {
     'obj': 'GMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full',
                     'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict_unsup')
    },
    {
     'obj': 'VBGMM',
     'init_params': {'n_components': 10, 'covariance_type': 'full',
                     'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit_unsup', 'predict_unsup')
    }
]

suite = _make_suite(_benchmarks)
