from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'DecisionTreeClassifier',
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'ExtraTreeClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
