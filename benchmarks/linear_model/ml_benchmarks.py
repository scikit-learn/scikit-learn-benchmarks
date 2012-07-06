from itertools import product

from vbench.benchmark import Benchmark

_setup = """
from sklearn.linear_model import %(estimator)s
from deps import load_data

kwargs = %(init_params)s
X, y, X_t, y_t = load_data('%(data)s')
est = %(estimator)s(**kwargs)
"""

_datasets = ['arcene', 'madelon']
_configurations = [
    {
     'estimator': 'LassoLars',
     'init_params': str({'alpha': 0.1, 'normalize': False}),
    },
    {
     'estimator': 'Lasso',
     'init_params': str({'alpha': 0.1, 'normalize': False}),
    },
    {
     'estimator': 'ElasticNet',
     'init_params': str({'rho': 0.5, 'alpha': 0.5}),  # normalize here?
    },
]

_all_configs = [dict(config, **{'name': config['estimator'] + '-' + data,
                                'data': data})
                for config, data in product(_configurations, _datasets)]

_fit_statement = "est.fit(X, y)"

_predict_statement = "est.predict(X_t)"

_globs = globals()
_globs.update({config['name'] + '-fit':
               Benchmark(_fit_statement, _setup % config, name=config['name'],
                         memory=True)
               for config in _all_configs})

_globs.update({config['name'] + '-predict':
               Benchmark(_predict_statement, _setup % config + _fit_statement,
                         name=config['name'], memory=True)
               for config in _all_configs})
