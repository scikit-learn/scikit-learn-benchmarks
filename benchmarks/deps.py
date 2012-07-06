# linear regression
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# logistic regression
from sklearn import linear_model
from sklearn.datasets.samples_generator import make_blobs


def load_data(dataset, data_dir="data"):
    """"
    Parameters
    ----------

    dataset : string
        Which dataset to load. Currently can be "madelon" or "arcene"
    """
    from numpy import fromfile, float64, int32
    f = open(data_dir + '/%s_train.data' % dataset)
    X = fromfile(f, dtype=float64, sep=' ')
    f.close()

    f = open(data_dir + '/%s_train.labels' % dataset)
    y = fromfile(f, dtype=int32, sep=' ')
    f.close()

    f = open(data_dir + '/%s_valid.data' % dataset)
    T = fromfile(f, dtype=float64, sep=' ')
    f.close()

    f = open(data_dir + '/%s_valid.labels' % dataset)
    valid = fromfile(f, dtype=float64, sep=' ')
    f.close()

    if dataset == 'madelon':
        X = X.reshape(-1, 500)
        T = T.reshape(-1, 500)
    elif dataset == 'arcene':
        X = X.reshape(-1, 10000)
        T = T.reshape(-1, 10000)

    return  X, y, T, valid
