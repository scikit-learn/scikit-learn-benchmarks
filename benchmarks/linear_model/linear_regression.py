from vbench.benchmark import Benchmark

setup = """
from deps import *

X, y = make_regression(1000, 1000, random_state=0)
lr = LinearRegression()
"""

statement = "lr.fit(X, y)"

linear_regression_dummy = Benchmark(statement, setup,
                                    name='linear_regression_dummy')
