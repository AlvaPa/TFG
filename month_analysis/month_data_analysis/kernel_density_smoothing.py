# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import numba


def smoothing(pollution, monthly_iqr):
    """"""
    h = np.array([0] * 12, dtype=float)
    quartic_function = np.array([[0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                 [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                 [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                 [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::])],
                                dtype=float)

    quartic_function = quartic_kernel(pollution, monthly_iqr, h, quartic_function)
    plotting(quartic_function, pollution)

    return


def plotting(quartic_function, pollution):
    """"""

    plt.figure(1)
    plt.plot(pollution[0, ::], quartic_function[0, ::])
    plt.show()


@numba.njit()
def quartic_kernel(pollution, monthly_iqr, h, quartic_function):
    """"""

    # We start computing the functions
    k_t = 0
    for i in range(0, 12):
        s = np.std(pollution[i, ::])
        h[i] = (2 * monthly_iqr[i]) / (3 * len(pollution[i, ::]) ** 0.2)
        pollution[i, ::] = np.sort(pollution[i, ::])
        for j in range(0, len(pollution[i, ::])):
            for k in range(0, len(pollution[i, ::])):
                t = (pollution[i, j] - pollution[i, k])
                if abs(t) < 1.0 and j != k:
                    k_t = k_t + 0.75 * (1 - t ** 2)
            quartic_function[i, j] = k_t / (h[i] * len(pollution[i, ::]))
            k_t = 0

    return quartic_function
