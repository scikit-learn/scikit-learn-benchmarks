from sklearn.datasets.samples_generator import make_blobs


def _load_data(data_dir="data"):
    # newsgroups: natural train/test split, first 100
    # blobs:
    # X, y = make_blobs(n_samples=500, n_features=50,
    #                   centers=10, center_box=(5, 20))
    # split 300-200
    from numpy import load
    from scipy.io import mmread
    from os.path import join

    data = {
        name: (load(join(data_dir, name, 'X_train.npy')),
               load(join(data_dir, name, 'y_train.npy')),
               load(join(data_dir, name, 'X_test.npy')),
               load(join(data_dir, name, 'y_test.npy')))
        for name in ('madelon', 'arcene', 'blobs')
    }

    data['newsgroups'] = (mmread(join(data_dir, 'newsgroups', 'X_train.mtx')),
                          load(join(data_dir, 'newsgroups', 'y_train.npy')),
                          mmread(join(data_dir, 'newsgroups', 'X_test.mtx')),
                          load(join(data_dir, 'newsgroups', 'y_test.npy')))
    return data

try:
    data = _load_data()
except:
    raise ValueError("Please extract the data before running the benchmarks.")

load_data = data.get
