from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'LabelSpreading',
     'spec': 'knn',
     'init_params': {'kernel': 'knn'},
     'datasets': ('arcene-semi', 'blobs-semi'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LabelSpreading',
     'spec': 'rbf',
     'init_params': {'kernel': 'rbf'},
     'datasets': ('arcene-semi', 'blobs-semi'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LabelPropagation',
     'spec': 'knn',
     'init_params': {'kernel': 'knn'},
     'datasets': ('arcene-semi', 'blobs-semi'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LabelPropagation',
     'spec': 'rbf',
     'init_params': {'kernel': 'rbf'},
     'datasets': ('arcene-semi', 'blobs-semi'),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
