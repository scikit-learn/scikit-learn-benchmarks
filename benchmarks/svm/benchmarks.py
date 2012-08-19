from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'SVC',
     'spec': 'linear',
     'init_params': {'kernel': 'linear'},
     'datasets': ('minimadelon-oney',),
     'statements': ('fit',)
    },
    {
     'obj': 'SVC',
     'spec': 'poly',
     'init_params': {'kernel': 'poly'},
     'datasets': ('minimadelon-oney',),
     'statements': ('fit',)
    },
    {
     'obj': 'SVC',
     'spec': 'rbf',
     'init_params': {'kernel': 'rbf'},
     'datasets': ('minimadelon-oney', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'SVC',
     'spec': 'sigmoid',
     'init_params': {'kernel': 'sigmoid'},
     'datasets': ('minimadelon-oney',),
     'statements': ('fit',)
    },
    {
     'obj': 'LinearSVC',
     'init_params': {},
     'datasets': ('newsgroups', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'OneClassSVM',
     'init_params': {'kernel': 'rbf'},
     'datasets': ('madelon',),
     'statements': ('fit',)
    },
    #
    # SVR takes enormous time, why?
    #{
    # 'obj': 'SVR',
    # 'spec': 'linear',
    # 'init_params': {'kernel': 'linear'},
    # 'datasets': ('minimadelon-oney', 'madelon'),
    # 'statements': ('fit',)
    #},
    # {
    #  'obj': 'SVR',
    #  'spec': 'poly',
    #  'init_params': {'kernel': 'poly'},
    #  'datasets': ('minimadelon-oney', 'blobs'),
    #  'statements': ('fit',)
    # },
    # {
    #  'obj': 'SVR',
    #  'spec': 'rbf',
    #  'init_params': {'kernel': 'rbf'},
    #  'datasets': ('minimadelon-oney', 'blobs'),
    #  'statements': ('fit', 'predict')
    # },
    # {
    #  'obj': 'SVR',
    #  'spec': 'sigmoid',
    #  'init_params': {'kernel': 'sigmoid'},
    #  'datasets': ('minimadelon-oney', 'blobs'),
    #  'statements': ('fit',)
    # },
]

suite = _make_suite(_benchmarks)
