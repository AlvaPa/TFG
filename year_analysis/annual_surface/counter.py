# encoding utf-8 #

import numpy as np
import numba
from constants import *


def counter(pollution, name):
    """
    Main function where the other functions are called to classify the pollutant's concentration in order to compute the
    surface percentage affected by each concentration interval.
    :param pollution: Pollutant's concentration [ug / m^3]
    :param name: Pollutant's name
    :return: surface_percentage
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

    return surface_percentage


@numba.njit()
def no2_counting(pollution, counter_array):
    """
    Function made to classify the NO2 concentration among intervals.
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


def ozone_counting(pollution, counter_array):
    """
    Function made to classify the ozone concentration among intervals.
    :param pollution: Pollutant's concentration
    :param counter_array: Array where we count the groups we have
    :return:
    """

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 50.0:
            counter_array[0] += 1
        elif 50.0 <= pollution[i] < 65.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def pm10_counting(pollution, counter_array):
    """
    Function made to classify the PM10 concentration among intervals.
    :param pollution: Pollutant's concentration
    :param counter_array: Array where we count the groups we have
    :return:
    """

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 20.0:
            counter_array[0] += 1
        elif 20.0 <= pollution[i] < 40.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def pm2p5_counting(pollution, counter_array):
    """
    Function made to classify the PM2.5 concentration among intervals.
    :param pollution: Pollutant's concentration
    :param counter_array: Array where we count the groups we have
    :return:
    """

    # We perform the iterations to start counting
    for i in range(0, len(pollution)):
        if pollution[i] < 10.0:
            counter_array[0] += 1
        elif 10.0 <= pollution[i] < 25.0:
            counter_array[1] += 1
        else:
            counter_array[2] += 1

    return counter_array


def surface_percentage_calculation(pollution, counter_array, surface_percentage):
    """
    Function made to compute the surface percentage affected by each interval of concentration
    :param pollution: Pollutant's concentration [ug / m^3]
    :param counter_array: Array which counts the locations affected by each interval of concentration
    :param surface_percentage: surface percentage affected by each interval of concentration
    :return: surface_percentage
    """

    # We compute the percentage of surface for each pollutant's concentration
    for i in range(0, len(counter_array)):
        surface_percentage[i] = round(100.0 * (float(counter_array[i]) / float(len(pollution))), 2)

    return surface_percentage
