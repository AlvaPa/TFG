# encoding utf-8 #

import numpy as np
import numba


def monthly_analysis(data_index, data_lon, data_lat, data_month, data_pollutant):
    """

    :param data_index:
    :param data_lon:
    :param data_lat:
    :param data_month:
    :param data_pollutant:
    :return:
    """

    "Variable's initialization"
    # Arrays made for sorting the data through months (and computing the median of each month)
    # Size of the arrays
    size = int(12 * len(data_month) / 365)
    # Index of the location
    index = np.array([0] * size, dtype=int)
    # Longitude of the location
    lon = np.array([0] * size, dtype=float)
    # Latitude of the location
    lat = np.array([0] * size, dtype=float)
    # Month
    month = np.array([0] * size, dtype=int)
    # Monthly median of the pollutant's concentration of each location [ug/m^3]
    pollution = np.array([0] * size, dtype=float)
    # Array that contains the pollutant of each day
    monthly_pollution = np.array([np.nan] * 31)
    m = 0

    # Arrays made for the statistical analysis
    # Sorted index
    sorted_index = np.array([0] * size, dtype=int)
    # Sorted lon
    sorted_lon = np.array([0] * size, dtype=float)
    # Sorted lat
    sorted_lat = np.array([0] * size, dtype=float)
    # Sorted month
    sorted_month = np.array([0] * size, dtype=int)
    # Sorted pollution [ug/m^3]
    sorted_pollution = np.array([0] * size, dtype=float)
    # We initialize the statistical variables to be computed
    # Median
    monthly_median = np.array([0] * 12, dtype=float)
    # Interquartile range
    monthly_iqr = np.array([0] * 12, dtype=float)
    # Yule-Kendall index
    monthly_yule_kendall = np.array([0] * 12, dtype=float)
    # Robust kurtosis
    monthly_robust_kurtosis = np.array([0] * 12, dtype=float)
    # Median of the pollution for every location for each month [ug/m^3]
    statistical_pollution = np.array([0] * int(len(data_month) / 365), dtype=float)

    "Sorting data through months and obtaining the median of each month"

    print('Sorting the data through months and obtaining the media of each month')
    for i in range(0, int(len(data_index) / 365)):
        # We separate the data for every location
        index, lon, lat, month, pollution, m = \
            monthly_separation(index, lon, lat, month, pollution, monthly_pollution, data_index, data_lon, data_lat,
                               data_month, data_pollutant, i, m)

    "Location statistical analysis"

    print('We compute the statistical variables')
    # We compute the statistical variables
    sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median, monthly_iqr, \
        monthly_yule_kendall, monthly_robust_kurtosis = \
        monthly_statistics(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median,
                           monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, statistical_pollution,
                           index, lon, lat, month, pollution)

    print('Median:', monthly_median, '\n', 'Interquartile range: ', monthly_iqr, '\n', 'Yule-Kendall index: ',
          monthly_yule_kendall, '\n', 'Robust kurtosis: ', monthly_robust_kurtosis)

    return


@numba.njit()
def monthly_separation(index, lon, lat, month, pollution, monthly_pollution, data_index, data_lon, data_lat, data_month,
                       data_pollutant, i, m):
    """
    This function returns the annual median of the pollutant's concentration for every given location, allowing us
    to later perform an statistical analysis of the location.
    :param index:
    :param lon:
    :param lat:
    :param month:
    :param pollution:
    :param monthly_pollution:
    :param data_index: Index to identify each location (longitude and latitude)
    :param data_lon: Longitude
    :param data_lat: Latitude
    :param data_month: Month
    :param data_pollutant: Mean of the day and location of the concentration of the pollutant [ug/m^3]
    :param i:
    :param m:
    :return: annual_index, annual_lon, annual_lat, annual_month, annual_day, annual_pollutant, j
    """

    # We initialize the variables
    j = i * 365
    # We separate each index according to it's spatial location
    k = 0
    # Index which counts the days passed in a year
    n = 0
    # Index which counts the days passed in a month
    x = 0
    # The condition becomes false when the year has finished
    condition = True

    while condition:
        for l in range(0, 364):
            monthly_pollution[x] = data_pollutant[l + j + n]
            k += 1
            x += 1
            # When the year or the month have finished, we stop the iteration
            if ((l + j + n + 1) % 365) == 0 or data_month[l + j + n] < data_month[l + j + n + 1]:
                x = 0
                break

        # We append the index, longitude, latitude, month and median of the pollution of each month to the variables
        index[m] = data_index[l + j + n]
        lon[m] = data_lon[l + j + n]
        lat[m] = data_lat[l + j + n]
        month[m] = data_month[l + j + n]
        pollution[m] = np.nanmedian(monthly_pollution)

        # If the year has ended, we stop the while loop
        if data_month[l + n] == 12:
            condition = False
        # We count the days of the year which have passed
        n = n + k
        m += 1
        k = 0
        for z in range(0, len(monthly_pollution)):
            monthly_pollution[z] = np.nan

    return index, lon, lat, month, pollution, m


def monthly_statistics(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median,
                       monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, statistical_pollution,
                       index, lon, lat, month, pollution):
    """
    This function sorts all the arrays gathered from month separation by month, and also computes the statistical
    variables for each pollution concentration per month for every location.
    :param sorted_index:
    :param sorted_lon:
    :param sorted_lat:
    :param sorted_month:
    :param sorted_pollution:
    :param monthly_median:
    :param monthly_iqr:
    :param monthly_yule_kendall:
    :param monthly_robust_kurtosis:
    :param statistical_pollution:
    :param index: Index of the location
    :param lon: Longitude of the location
    :param lat: Latitude of the location
    :param month: Month
    :param pollution: Monthly median of the pollutant's concentration of each location [ug/m^3]
    :return: sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median, monthly_iqr, \
        monthly_yule_kendall, monthly_robust_kurtosis
    """
    # Number of locations to compute
    n = int(len(month) / 12)
    # Month counter
    m = 0
    # Total counter
    j = 0
    i = 0

    while m < 12:
        for k in range(0, n - 1):
            sorted_index[k + j] = index[12 * k + m]
            sorted_lon[k + j] = lon[12 * k + m]
            sorted_lat[k + j] = lat[12 * k + m]
            sorted_month[k + j] = month[12 * k + m]
            sorted_pollution[k + j] = pollution[12 * k + m]
            statistical_pollution[k] = pollution[12 * k + m]
            i += 1

        monthly_median[m] = np.median(statistical_pollution)
        monthly_iqr[m] = np.quantile(statistical_pollution, 0.75) - np.quantile(statistical_pollution, 0.25)
        monthly_yule_kendall[m] = (np.quantile(statistical_pollution, 0.75) + np.quantile(statistical_pollution, 0.25)
                                   - 2 * monthly_median[m]) / monthly_iqr[m]
        monthly_robust_kurtosis[m] = monthly_iqr[m] / (2 * (np.quantile(statistical_pollution, 0.9) -
                                                            np.quantile(statistical_pollution, 0.10)))
        m += 1
        j += i
        i = 0

    return sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median, monthly_iqr, \
        monthly_yule_kendall, monthly_robust_kurtosis
