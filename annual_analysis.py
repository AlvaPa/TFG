# encoding utf-8 #

import numpy as np


def annual_analysis(data_index, data_lon, data_lat, data_pollutant):
    """
    This is the main function that performs the statistical analysis of the pollutant according to the spatial location,
    and gives the annual mean for every location. It then writes a file with all the values computed before.
    :param data_index: Index to identify each location (longitude and latitude)
    :param data_lon: Longitude
    :param data_lat: Latitude
    :param data_pollutant: Mean of the day and location of the concentration of the pollutant
    :return:
    """

    # We initialize the variables necessary to perform the analysis
    # Value to read through each location of the data
    j = 0
    # Index of each location
    index = np.array([], dtype=int)
    # Longitude of each location
    lon = np.array([], dtype=float)
    # Latitude of each location
    lat = np.array([], dtype=float)
    # Annual median of the pollutant's concentration of each location [ug/m^3]
    pollutant = np.array([], dtype=float)

    # We divide the data per location
    for i in range(0, 151428):
        # We read the file and get the mean pollution for every location
        current_index, current_lon, current_lat, current_mean_pollution, j = \
            location_separation(data_index, data_lon, data_lat, data_pollutant, j)
        index = np.append(index, current_index)
        lon = np.append(lon, current_lon)
        lat = np.append(lat, current_lat)
        pollutant = np.append(pollutant, current_mean_pollution)

    # We compute the statistical variables of the pollution for every location
    annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis = statistics(pollutant)


def location_separation(data_index, data_lon, data_lat, data_pollutant, j):
    """
    This function returns the annual median of the pollutant's concentration for every given location, allowing us
    to later perform an statistical analysis of the location.
    :param data_index: Index to identify each location (longitude and latitude)
    :param data_lon: Longitude
    :param data_lat: Latitude
    :param data_pollutant: Mean of the day and location of the concentration of the pollutant [ug/m^3]
    :param j: Parameter used to read all the file.
    :return: current_index, current_lon, current_lat, current_mean_pollution, j
    """

    # We initialize the variables
    # Pollution's concentration in a certain location per year [ug/m^3]
    pollutant = np.array([], dtype=float)

    # We separate each index according to it's spatial location
    k = 0
    for i in range(0, 364):
        pollutant = np.append(pollutant, data_pollutant[i + j])
        k += 1

    # We equal k and j to be ready for the next iteration
    j = j + k + 1
    # Index of the location
    current_index = data_index[k]
    # Longitude of the location
    current_lon = data_lon[k]
    # Latitude of the location
    current_lat = data_lat[k]
    # Mean pollution's concentration of the given location [ug/m^3]
    current_mean_pollution = np.median(pollutant)

    return current_index, current_lon, current_lat, current_mean_pollution, j


def statistics(pollutant):
    """
    This function computes the statistical variables of the pollutant per location.
    :param pollutant: Median of each pollution's concentration per location [ug/m^3]
    :return: annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis
    """

    # We compute the statistical variables
    # Median [ug/m^3]
    annual_median = np.median(pollutant)
    # Interquartile range [ug/m^3]
    annual_iqr = np.quantile(pollutant, 0.75) - np.quantile(pollutant, 0.25)
    # Yule-Kendall index
    annual_yule_kendall = \
        (np.quantile(pollutant, 0.75) + np.quantile(pollutant, 0.25) - 2 * np.median(pollutant)) / annual_iqr
    # Robust kurtosis
    annual_robust_kurtosis = annual_iqr / (2 * (np.quantile(pollutant, 0.9) - np.quantile(pollutant, 0.1)))

    return annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis


def output_file(index, lon, lat, pollutant, annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis):
    """

    :param index: Index of each location
    :param lon: Longitude of each location
    :param lat: Latitude of each location
    :param pollutant: Annual median of the pollutant's concentration of each location [ug/m^3]
    :param annual_median: Median [ug/m^3]
    :param annual_iqr: Interquartile range [ug/m^3]
    :param annual_yule_kendall: Yule-Kendall index
    :param annual_robust_kurtosis: Robust kurtosis
    :return:
    """
