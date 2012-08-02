from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'CCA',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'transform')
    },
    {
     'obj': 'PLSCanonical',
     'init_params': {},
     'datasets': ('arcene', 'blobs'),
     'statements': ('fit', 'transform')
    },
    {
     'obj': 'PLSRegression',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'transform')
    }
]

suite = _make_suite(_benchmarks)
