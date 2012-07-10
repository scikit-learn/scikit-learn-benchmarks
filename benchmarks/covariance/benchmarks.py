from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'GraphLasso',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'MCD',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'ShrunkCovariance',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'LedoitWolf',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'OAS',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
]

suite = _make_suite(_benchmarks)
