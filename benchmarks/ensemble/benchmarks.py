from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'RandomForestClassifier',
     'init_params': {'random_state': 0},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'ExtraTreesClassifier',
     'init_params': {'random_state': 0},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
    {
     'obj': 'GradientBoostingClassifier',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit',)
    },
]

suite = _make_suite(_benchmarks)
