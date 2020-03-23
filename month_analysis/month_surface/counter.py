# encoding utf-8 #

import numpy as np
import numba
from constants import *


def counter(lon, lat, pollution, name):
    """
    Main function where the other functions are called to classify the pollutant's concentration
    :param lon: Longitude
    :param lat: Latitude
    :param pollution: Pollutant's concentration [ug / m^3]
    :param name: Pollutant's name
    :return:
    """

    # We initialize some variables to perform the counting
    # Counter
    counter_array = np.array([0] * 16, dtype=int)
    # Surface percentage
    surface_percentage = np.array([0.0] * 16, dtype=float)

    # We perform the counting
    if name == no2:
        counter_array = no2_counting(pollution, counter_array)
    elif name == ozone:
        counter_array = ozone_counting(pollution, counter_array)
    elif name == pm_10:
        counter_array = pm10_counting(pollution, counter_array)
    else:
        counter_array = pm2p5_counting(pollution, counter_array)

    # We perform the surface percentage calculation for each pollutant's concentration
    surface_percentage = surface_percentage_calculation(pollution, counter_array, surface_percentage)

    # Longitude classified by concentration
    classified_lon = np.array([np.array([0] * counter_array[0], dtype=float),
                               np.array([0] * counter_array[1], dtype=float),
                               np.array([0] * counter_array[2], dtype=float),
                               np.array([0] * counter_array[3], dtype=float),
                               np.array([0] * counter_array[4], dtype=float),
                               np.array([0] * counter_array[5], dtype=float),
                               np.array([0] * counter_array[6], dtype=float),
                               np.array([0] * counter_array[7], dtype=float),
                               np.array([0] * counter_array[8], dtype=float),
                               np.array([0] * counter_array[9], dtype=float),
                               np.array([0] * counter_array[10], dtype=float),
                               np.array([0] * counter_array[11], dtype=float),
                               np.array([0] * counter_array[12], dtype=float),
                               np.array([0] * counter_array[13], dtype=float),
                               np.array([0] * counter_array[14], dtype=float),
                               np.array([0] * counter_array[15], dtype=float)])
    # Latitude classified by concentration
    classified_lat = np.array([np.array([0] * counter_array[0], dtype=float),
                               np.array([0] * counter_array[1], dtype=float),
                               np.array([0] * counter_array[2], dtype=float),
                               np.array([0] * counter_array[3], dtype=float),
                               np.array([0] * counter_array[4], dtype=float),
                               np.array([0] * counter_array[5], dtype=float),
                               np.array([0] * counter_array[6], dtype=float),
                               np.array([0] * counter_array[7], dtype=float),
                               np.array([0] * counter_array[8], dtype=float),
                               np.array([0] * counter_array[9], dtype=float),
                               np.array([0] * counter_array[10], dtype=float),
                               np.array([0] * counter_array[11], dtype=float),
                               np.array([0] * counter_array[12], dtype=float),
                               np.array([0] * counter_array[13], dtype=float),
                               np.array([0] * counter_array[14], dtype=float),
                               np.array([0] * counter_array[15], dtype=float)])

    # We perform the classification
    if name == no2:
        classified_lon, classified_lat = \
            no2_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat)
    elif name == ozone:
        classified_lon, classified_lat = \
            ozone_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat)
    elif name == pm_10:
        classified_lon, classified_lat = \
            pm10_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat)
    else:
        classified_lon, classified_lat = \
            pm2p5_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat)

    return surface_percentage, classified_lon, classified_lat


@numba.njit()
def no2_counting(pollution, counter_array):
    """

    :param pollution: Pollutant's concentration
    :param counter_array: Array where we count the groups we have
    :return: counter_array
    """

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 5.0:
            counter_array[0] += 1
        elif 5.0 <= pollution[i] < 10.0:
            counter_array[1] += 1
        elif 10.0 <= pollution[i] < 15.0:
            counter_array[2] += 1
        elif 15.0 <= pollution[i] < 20.0:
            counter_array[3] += 1
        elif 20.0 <= pollution[i] < 25.0:
            counter_array[4] += 1
        elif 25.0 <= pollution[i] < 30.0:
            counter_array[5] += 1
        elif 30.0 <= pollution[i] < 35.0:
            counter_array[6] += 1
        elif 35.0 <= pollution[i] < 40.0:
            counter_array[7] += 1
        else:
            counter_array[8] += 1

    return counter_array


def no2_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 5.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 5.0 <= pollution[alpha] < 10.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        elif 10.0 <= pollution[alpha] < 15.0:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1
        elif 15.0 <= pollution[alpha] < 20.0:
            classified_lon[3][d] = lon[alpha]
            classified_lat[3][d] = lat[alpha]
            d += 1
        elif 20.0 <= pollution[alpha] < 25.0:
            classified_lon[4][e] = lon[alpha]
            classified_lat[4][e] = lat[alpha]
            e += 1
        elif 25.0 <= pollution[alpha] < 30.0:
            classified_lon[5][f] = lon[alpha]
            classified_lat[5][f] = lat[alpha]
            f += 1
        elif 30.0 <= pollution[alpha] < 35.0:
            classified_lon[6][g] = lon[alpha]
            classified_lat[6][g] = lat[alpha]
            g += 1
        elif 35.0 <= pollution[alpha] < 40.0:
            classified_lon[7][h] = lon[alpha]
            classified_lat[7][h] = lat[alpha]
            h += 1
        else:
            classified_lon[8][i] = lon[alpha]
            classified_lat[8][i] = lat[alpha]
            i += 1

    return classified_lon, classified_lat


def ozone_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 10.0:
            counter_array[0] += 1
        elif 10.0 <= pollution[i] < 20.0:
            counter_array[1] += 1
        elif 20.0 <= pollution[i] < 30.0:
            counter_array[2] += 1
        elif 30.0 <= pollution[i] < 40.0:
            counter_array[3] += 1
        elif 40.0 <= pollution[i] < 50.0:
            counter_array[4] += 1
        elif 50.0 <= pollution[i] < 60.0:
            counter_array[5] += 1
        elif 60.0 <= pollution[i] < 70.0:
            counter_array[6] += 1
        elif 70.0 <= pollution[i] < 80.0:
            counter_array[7] += 1
        elif 80.0 <= pollution[i] < 90.0:
            counter_array[8] += 1
        elif 90.0 <= pollution[i] < 100.0:
            counter_array[9] += 1
        elif 100.0 <= pollution[i] < 110.0:
            counter_array[10] += 1
        elif 110.0 <= pollution[i] < 120.0:
            counter_array[11] += 1
        else:
            counter_array[12] += 1

    return counter_array


def ozone_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    m = 0
    n = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 10.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 10.0 <= pollution[alpha] < 20.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        elif 20.0 <= pollution[alpha] < 30.0:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1
        elif 30.0 <= pollution[alpha] < 40.0:
            classified_lon[3][d] = lon[alpha]
            classified_lat[3][d] = lat[alpha]
            d += 1
        elif 40.0 <= pollution[alpha] < 50.0:
            classified_lon[4][e] = lon[alpha]
            classified_lat[4][e] = lat[alpha]
            e += 1
        elif 50.0 <= pollution[alpha] < 60.0:
            classified_lon[5][f] = lon[alpha]
            classified_lat[5][f] = lat[alpha]
            f += 1
        elif 60.0 <= pollution[alpha] < 70.0:
            classified_lon[6][g] = lon[alpha]
            classified_lat[6][g] = lat[alpha]
            g += 1
        elif 70.0 <= pollution[alpha] < 80.0:
            classified_lon[7][h] = lon[alpha]
            classified_lat[7][h] = lat[alpha]
            h += 1
        elif 80.0 <= pollution[alpha] < 90.0:
            classified_lon[8][i] = lon[alpha]
            classified_lat[8][i] = lat[alpha]
            i += 1
        elif 90.0 <= pollution[alpha] < 100.0:
            classified_lon[9][j] = lon[alpha]
            classified_lat[9][j] = lat[alpha]
            j += 1
        elif 100.0 <= pollution[alpha] < 110.0:
            classified_lon[10][k] = lon[alpha]
            classified_lat[10][k] = lat[alpha]
            k += 1
        elif 110.0 <= pollution[alpha] < 120.0:
            classified_lon[11][m] = lon[alpha]
            classified_lat[11][m] = lat[alpha]
            m += 1
        else:
            classified_lon[12][n] = lon[alpha]
            classified_lat[12][n] = lat[alpha]
            n += 1

    return classified_lon, classified_lat


def pm10_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 12.0:
            counter_array[0] += 1
        elif 12.0 <= pollution[i] < 14.0:
            counter_array[1] += 1
        elif 14.0 <= pollution[i] < 16.0:
            counter_array[2] += 1
        elif 16.0 <= pollution[i] < 18.0:
            counter_array[3] += 1
        elif 18.0 <= pollution[i] < 20.0:
            counter_array[4] += 1
        elif 20.0 <= pollution[i] < 22.0:
            counter_array[5] += 1
        elif 22.0 <= pollution[i] < 24.0:
            counter_array[6] += 1
        elif 24.0 <= pollution[i] < 26.0:
            counter_array[7] += 1
        elif 26.0 <= pollution[i] < 28.0:
            counter_array[8] += 1
        elif 28.0 <= pollution[i] < 30.0:
            counter_array[9] += 1
        elif 30.0 <= pollution[i] < 32.0:
            counter_array[10] += 1
        elif 32.0 <= pollution[i] < 34.0:
            counter_array[11] += 1
        elif 34.0 <= pollution[i] < 36.0:
            counter_array[12] += 1
        elif 36.0 <= pollution[i] < 38:
            counter_array[13] += 1
        elif 38.0 <= pollution[i] < 40.0:
            counter_array[14] += 1
        else:
            counter_array[15] += 1

    return counter_array


def pm10_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 12.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 12.0 <= pollution[alpha] < 14.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        elif 14.0 <= pollution[alpha] < 16.0:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1
        elif 16.0 <= pollution[alpha] < 18.0:
            classified_lon[3][d] = lon[alpha]
            classified_lat[3][d] = lat[alpha]
            d += 1
        elif 18.0 <= pollution[alpha] < 20.0:
            classified_lon[4][e] = lon[alpha]
            classified_lat[4][e] = lat[alpha]
            e += 1
        elif 20.0 <= pollution[alpha] < 22.0:
            classified_lon[5][f] = lon[alpha]
            classified_lat[5][f] = lat[alpha]
            f += 1
        elif 22.0 <= pollution[alpha] < 24.0:
            classified_lon[6][g] = lon[alpha]
            classified_lat[6][g] = lat[alpha]
            g += 1
        elif 24.0 <= pollution[alpha] < 26.0:
            classified_lon[7][h] = lon[alpha]
            classified_lat[7][h] = lat[alpha]
            h += 1
        elif 26.0 <= pollution[alpha] < 28.0:
            classified_lon[8][i] = lon[alpha]
            classified_lat[8][i] = lat[alpha]
            i += 1
        elif 28.0 <= pollution[alpha] < 30.0:
            classified_lon[9][j] = lon[alpha]
            classified_lat[9][j] = lat[alpha]
            j += 1
        elif 30.0 <= pollution[alpha] < 32.0:
            classified_lon[10][k] = lon[alpha]
            classified_lat[10][k] = lat[alpha]
            k += 1
        elif 32.0 <= pollution[alpha] < 34.0:
            classified_lon[11][m] = lon[alpha]
            classified_lat[11][m] = lat[alpha]
            m += 1
        elif 34.0 <= pollution[alpha] < 36.0:
            classified_lon[12][n] = lon[alpha]
            classified_lat[12][n] = lat[alpha]
            n += 1
        elif 36.0 <= pollution[alpha] < 38.0:
            classified_lon[13][o] = lon[alpha]
            classified_lat[13][o] = lat[alpha]
            o += 1
        elif 38.0 <= pollution[alpha] < 40.0:
            classified_lon[14][p] = lon[alpha]
            classified_lat[14][p] = lat[alpha]
            p += 1
        else:
            classified_lon[15][q] = lon[alpha]
            classified_lat[15][q] = lat[alpha]
            q += 1

    return classified_lon, classified_lat


def pm2p5_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 6.0:
            counter_array[0] += 1
        elif 6.0 <= pollution[i] < 7.0:
            counter_array[1] += 1
        elif 7.0 <= pollution[i] < 8.0:
            counter_array[2] += 1
        elif 8.0 <= pollution[i] < 9.0:
            counter_array[3] += 1
        elif 9.0 <= pollution[i] < 10.0:
            counter_array[4] += 1
        elif 10.0 <= pollution[i] < 11.0:
            counter_array[5] += 1
        elif 11.0 <= pollution[i] < 12.0:
            counter_array[6] += 1
        elif 12.0 <= pollution[i] < 13.0:
            counter_array[7] += 1
        elif 13.0 <= pollution[i] < 14.0:
            counter_array[8] += 1
        elif 14.0 <= pollution[i] < 15.0:
            counter_array[9] += 1
        elif 15.0 <= pollution[i] < 16.0:
            counter_array[10] += 1
        elif 16.0 <= pollution[i] < 17.0:
            counter_array[11] += 1
        elif 17.0 <= pollution[i] < 18.0:
            counter_array[12] += 1
        elif 18.0 <= pollution[i] < 19.0:
            counter_array[13] += 1
        elif 19.0 <= pollution[i] < 20.0:
            counter_array[14] += 1
        else:
            counter_array[15] += 1

    return counter_array


def pm2p5_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 6.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 6.0 <= pollution[alpha] < 7.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        elif 7.0 <= pollution[alpha] < 8.0:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1
        elif 8.0 <= pollution[alpha] < 9.0:
            classified_lon[3][d] = lon[alpha]
            classified_lat[3][d] = lat[alpha]
            d += 1
        elif 9.0 <= pollution[alpha] < 10.0:
            classified_lon[4][e] = lon[alpha]
            classified_lat[4][e] = lat[alpha]
            e += 1
        elif 10.0 <= pollution[alpha] < 11.0:
            classified_lon[5][f] = lon[alpha]
            classified_lat[5][f] = lat[alpha]
            f += 1
        elif 11.0 <= pollution[alpha] < 12.0:
            classified_lon[6][g] = lon[alpha]
            classified_lat[6][g] = lat[alpha]
            g += 1
        elif 12.0 <= pollution[alpha] < 13.0:
            classified_lon[7][h] = lon[alpha]
            classified_lat[7][h] = lat[alpha]
            h += 1
        elif 13.0 <= pollution[alpha] < 14.0:
            classified_lon[8][i] = lon[alpha]
            classified_lat[8][i] = lat[alpha]
            i += 1
        elif 14.0 <= pollution[alpha] < 15.0:
            classified_lon[9][j] = lon[alpha]
            classified_lat[9][j] = lat[alpha]
            j += 1
        elif 15.0 <= pollution[alpha] < 16.0:
            classified_lon[10][k] = lon[alpha]
            classified_lat[10][k] = lat[alpha]
            k += 1
        elif 16.0 <= pollution[alpha] < 17.0:
            classified_lon[11][m] = lon[alpha]
            classified_lat[11][m] = lat[alpha]
            m += 1
        elif 17.0 <= pollution[alpha] < 18.0:
            classified_lon[12][n] = lon[alpha]
            classified_lat[12][n] = lat[alpha]
            n += 1
        elif 18.0 <= pollution[alpha] < 19.0:
            classified_lon[13][o] = lon[alpha]
            classified_lat[13][o] = lat[alpha]
            o += 1
        elif 19.0 <= pollution[alpha] < 20.0:
            classified_lon[14][p] = lon[alpha]
            classified_lat[14][p] = lat[alpha]
            p += 1
        else:
            classified_lon[15][q] = lon[alpha]
            classified_lat[15][q] = lat[alpha]
            q += 1

    return classified_lon, classified_lat


def surface_percentage_calculation(pollution, counter_array, surface_percentage):
    """"""

    # We compute the percentage of surface for each pollutant's concentration
    for i in range(0, len(counter_array)):
        surface_percentage[i] = 100.0 * (float(counter_array[i]) / float(len(pollution)))

    return surface_percentage
