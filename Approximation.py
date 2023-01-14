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


def get_coefficients(A, B):
    return np.dot(B, np.linalg.inv(A))


def show_graph(xlim, ylim, coefficients):
    import matplotlib.pyplot as plt

    x = np.linspace(*xlim, (abs(xlim[0]) + abs(xlim[1])) * 2)
    y = coefficients[0] + coefficients[1] * x + + coefficients[2] * x ** 2 + coefficients[3] * x ** 3

    plt.plot(x, y, label='f(x)')

    # Add features to our figure
    plt.legend()
    plt.grid(True, linestyle='-')
    plt.xlim(xlim)
    plt.ylim(ylim)

    plt.title('f(x) = a0 + a1x + a2x^2 + a3x^3')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # Show plot
    plt.show()
