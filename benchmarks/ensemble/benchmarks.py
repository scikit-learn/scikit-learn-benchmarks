from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'RandomForestClassifier',
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'ExtraTreesClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'GradientBoostingClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
