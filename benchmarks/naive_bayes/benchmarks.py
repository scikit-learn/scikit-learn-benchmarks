from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'BernoulliNB',
     'init_params': {'binarize': 1},
     'datasets': ('newsgroups',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'BernoulliNB',
     'init_params': {'binarize': 500},
     'datasets': ('madelon',),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'MultinomialNB',
     'init_params': {},
     'datasets': ('newsgroups', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'GaussianNB',
     'init_params': {},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
]

suite = _make_suite(_benchmarks)
