from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'KMeans',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'MiniBatchKMeans',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'SpectralClustering',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'Ward',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    },
    {
     'obj': 'MeanShift',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'AffinityPropagation',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit',)
    }
]

suite = _make_suite(_benchmarks)
