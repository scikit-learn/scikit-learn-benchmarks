from itertools import product

from vbench.benchmark import Benchmark

_setup = """
from sklearn.decomposition import %(transformer)s
from deps import load_data

kwargs = %(init_params)s
X, y, X_t, y_t = load_data('%(data)s')
trf = %(transformer)s(**kwargs)
"""

_datasets = ['arcene', 'madelon']
_configurations = [
    {
     'transformer': 'PCA',
     'init_params': str({'n_components': 9}),
    },
    {
     'transformer': 'RandomizedPCA',
     'init_params': str({'n_components': 9}),
    },
    {
     'transformer': 'FastICA',
     'spec': 'deflation',
     'init_params': str({'n_components': 9, 'algorithm': 'deflation'}),
    },
    {
     'transformer': 'FastICA',
     'spec': 'parallel',
     'init_params': str({'n_components': 9, 'algorithm': 'parallel'}),
    },
#    Horribly slow!
#    {
#     'transformer': 'NMF',
#     'init_params': str({'n_components': 9}),
#    },
]

_all_configs = [dict(config, **{'name': '-'.join(
                                             filter(lambda x: x is not None,
                                                    (config['transformer'],
                                                     config.get('spec'), data))
                                                ),
                                'data': data})
                for config, data in product(_configurations, _datasets)]

_fit_statement = "trf.fit(X)"

_transform_statement = "trf.transform(X)"

_fit_transform_statement = "trf.fit_transform(X)"

_globs = globals()
_globs.update({config['name'] + '-fit':
              Benchmark(_fit_statement, _setup % config,
                        name=config['name'] + '-fit', memory=True)
              for config in _all_configs})

_globs.update({config['name'] + '-transform':
              Benchmark(_transform_statement, _setup % config + _fit_statement,
                         name=config['name'] + '-transform', memory=True)
              for config in _all_configs})

_globs.update({config['name'] + '-fit_transform':
              Benchmark(_fit_transform_statement, _setup % config,
                         name=config['name'] + '-fit_transform', memory=True)
              for config in _all_configs})
