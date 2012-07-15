from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'KMeans',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'predict_unsup')
    },
    {
     'obj': 'MiniBatchKMeans',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit_unsup', 'predict_unsup')
    },
    {
     'obj': 'SpectralClustering',
     'init_params': {'n_clusters': 9},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'predict_unsup')
    },
    {
     'obj': 'Ward',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup',)
    },
    {
     'obj': 'MeanShift',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit_unsup', 'predict_unsup')
    },
#    {
#     'obj': 'AffinityPropagation',
#     'init_params': {},
#     'datasets': ('minimadelon', 'blobs'),
#     'statements': ('fit_unsup',)
#    }
]

suite = _make_suite(_benchmarks)
