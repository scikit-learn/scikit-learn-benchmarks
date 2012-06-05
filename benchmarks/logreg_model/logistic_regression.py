from vbench.benchmark import Benchmark

setup = """
from deps import *

X, y = make_blobs(n_samples=50, centers=3, n_features=10, random_state=0)
logreg = linear_model.LogisticRegression(C=1e5)
"""
statement = "logreg.fit(X, y)"

logistic_regression_dummy = Benchmark(statement, setup,
                                    name='logistic_regression_dummy')
