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
    counter_array = np.array([0] * 3, dtype=int)
    # Surface percentage
    surface_percentage = np.array([0.0] * 3, dtype=float)

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
                               np.array([0] * counter_array[2], dtype=float)])
    # Latitude classified by concentration
    classified_lat = np.array([np.array([0] * counter_array[0], dtype=float),
                               np.array([0] * counter_array[1], dtype=float),
                               np.array([0] * counter_array[2], dtype=float)])

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
        if pollution[i] < 40.0:
            counter_array[0] += 1
        else:
            counter_array[2] += 1

    return counter_array


def no2_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 40.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        else:
            classified_lon[2][b] = lon[alpha]
            classified_lat[2][b] = lat[alpha]
            b += 1

    return classified_lon, classified_lat


def ozone_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 50.0:
            counter_array[0] += 1
        elif 50.0 <= pollution[i] < 65.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def ozone_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 50.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 50.0 <= pollution[alpha] < 65.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        else:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1

    return classified_lon, classified_lat


def pm10_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 20.0:
            counter_array[0] += 1
        elif 20.0 <= pollution[i] < 40.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def pm10_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 20.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 20.0 <= pollution[alpha] < 40.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        else:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1

    return classified_lon, classified_lat


def pm2p5_counting(pollution, counter_array):
    """"""

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 10.0:
            counter_array[0] += 1
        elif 10.0 <= pollution[i] < 25.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def pm2p5_coordinates_classification(lon, lat, pollution, classified_lon, classified_lat):
    """"""

    # We initialize some variables to perform the iterations
    a = 0
    b = 0
    c = 0

    # We start the iteration to classify
    for alpha in range(0, len(pollution)):
        if pollution[alpha] < 10.0:
            classified_lon[0][a] = lon[alpha]
            classified_lat[0][a] = lat[alpha]
            a += 1
        elif 10.0 <= pollution[alpha] < 25.0:
            classified_lon[1][b] = lon[alpha]
            classified_lat[1][b] = lat[alpha]
            b += 1
        else:
            classified_lon[2][c] = lon[alpha]
            classified_lat[2][c] = lat[alpha]
            c += 1

    return classified_lon, classified_lat


def surface_percentage_calculation(pollution, counter_array, surface_percentage):
    """"""

    # We compute the percentage of surface for each pollutant's concentration
    for i in range(0, len(counter_array)):
        surface_percentage[i] = round(100.0 * (float(counter_array[i]) / float(len(pollution))), 2)

    return surface_percentage
