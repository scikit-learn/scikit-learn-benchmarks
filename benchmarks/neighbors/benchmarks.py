from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'KNeighborsClassifier',
     'spec': 'brute',
     'init_params': {'n_neighbors': 5, 'algorithm': 'brute'},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('predict',)
    },
    {
     'obj': 'KNeighborsClassifier',
     'spec': 'ball_tree',
     'init_params': {'n_neighbors': 5, 'algorithm': 'ball_tree'},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'RadiusNeighborsClassifier',
     'spec': 'brute',
     'init_params': {'algorithm': 'brute', 'radius': 500.0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'RadiusNeighborsClassifier',
     'spec': 'ball_tree',
     'init_params': {'algorithm': 'ball_tree', 'radius': 500.0},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'NearestCentroid',
     'init_params': {},
     'datasets': ('madelon',),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
