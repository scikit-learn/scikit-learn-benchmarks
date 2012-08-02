from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'GraphLasso',
     'init_params': {},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup',)
    },
    {
     'obj': 'MinCovDet',
     'init_params': {},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup',)
    },
    {
     'obj': 'ShrunkCovariance',
     'init_params': {},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup',)
    },
    {
     'obj': 'LedoitWolf',
     'init_params': {},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup',)
    },
    {
     'obj': 'OAS',
     'init_params': {},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup',)
    },
]

suite = _make_suite(_benchmarks)
