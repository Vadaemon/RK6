import numpy as np

n = 4


def set_X(arr_x):
    return np.array(arr_x)


def set_Y(arr_y):
    return np.array(arr_y)


def pprint_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()


def get_det(x):
    return np.array([
        [n, sum(x), sum(x ** 2), sum(x ** 3)],
        [sum(x), sum(x ** 2), sum(x ** 3), sum(x ** 4)],
        [sum(x ** 2), sum(x ** 3), sum(x ** 4), sum(x ** 5)],
        [sum(x ** 3), sum(x ** 4), sum(x ** 5), sum(x ** 6)]
    ])


def get_b(x, y):
    return np.array([
        sum(y), sum(y * x), sum(y * x ** 2), sum(y * x ** 3)
    ])
