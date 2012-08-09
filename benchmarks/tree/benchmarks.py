from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'DecisionTreeClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'ExtraTreeClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
]

suite = _make_suite(_benchmarks)
