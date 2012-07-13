def _load_data(data_dir="data"):
    """Prepares the data for benchmarks.

    Available datasets:

    -- arcene: (900, 10000)  TODO: split?
    -- madelon: (4400, 500)  TODO: split?
    -- minimadelon: (30:20, 500)
    -- blobs: (300, 50) and (200, 50), 10 centers
    -- newsgroups: first 100 vectorized documents from test and train

    minimadelon was generated with:
    X, y = make_classification(50, 500, n_informative=20, n_repeated=20,
                               n_redundant=20, random_state=0)
    Then, y was copied 10 times, and each column was flipped in 0.2 positions:
    rng = np.random.RandomState(0)
    rng.random_integers(0, len(y) - 1, (10, int(0.2 * len(y))))
    flipping code is as expected.

    """
    from numpy import load
    from scipy.io import mmread
    from os.path import join

    data = dict(
        [(name, (load(join(data_dir, name, 'X_train.npy')),
               load(join(data_dir, name, 'y_train.npy')),
               load(join(data_dir, name, 'X_test.npy')),
               load(join(data_dir, name, 'y_test.npy'))))
        for name in ('madelon', 'minimadelon', 'arcene', 'blobs')
    ])

    data['newsgroups'] = (mmread(join(data_dir, 'newsgroups', 'X_train.mtx')),
                          load(join(data_dir, 'newsgroups', 'y_train.npy')),
                          mmread(join(data_dir, 'newsgroups', 'X_test.mtx')),
                          load(join(data_dir, 'newsgroups', 'y_test.npy')))
    return data

try:
    data = _load_data()
except:
    raise ValueError("Please extract the data before running the benchmarks.")


def load_data(name):
    params = name.split('-')
    Xtr, ytr, Xte, yte = data.get(params[0])
    if len(params) > 1:
        if params[-1] == 'oney':
            # keep only the first y in a multi-output scenario
            ytr = ytr.copy()[:, 0]
            yte = yte.copy()[:, 0]
        if params[-1] == 'semi':
            # unlabel some data
            import numpy as np
            ytr = ytr.copy()
            yte = yte.copy()
            for y in (ytr, yte):
                rng = np.random.RandomState(0)
                indices = np.where(rng.random_integers(0, 1, size=len(y)))
                #y = y.copy()
                y[indices] = -1
    return Xtr, ytr, Xte, yte
