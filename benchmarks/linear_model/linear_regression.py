from vbench.benchmark import Benchmark

_setup = """
from deps import *

kwargs = %s
X, y = make_regression(random_state=0, **kwargs)
lr = LinearRegression()
"""

_configurations = [
    ('linear_regression_many_samples',
     {'n_samples': 10000, 'n_features': 100}),
    ('linear_regression_many_features',
     {'n_samples': 100, 'n_features': 10000}),
    ('linear_regression_many_targets',
     {'n_samples': 1000, 'n_features': 100, 'n_targets': 100})
    ]

_statement = "lr.fit(X, y)"

_globs = globals()
_globs.update({name: Benchmark(_statement, _setup % str(kwargs), name=name,
                               memory=True)
              for name, kwargs in _configurations})

