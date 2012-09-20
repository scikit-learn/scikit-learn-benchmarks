from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'GaussianProcess',
     'spec': 'cobyla',
     'init_params': {'optimizer': 'fmin_cobyla', 'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'GaussianProcess',
     'spec': 'Welch',
     'init_params': {'optimizer': 'Welch', 'random_state': 0},
     'datasets': ('blobs',),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
