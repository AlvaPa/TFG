# encoding utf-8 #

import numpy as np
import numba


def monthly_analysis(data_index, data_lon, data_lat, data_month, data_pollutant, days):
    """

    :param data_index: Index provided by the text file
    :param data_lon: Longitude provided by the text file
    :param data_lat: Latitude provided by the text file
    :param data_month: Month provided by the text file
    :param data_pollutant: Daily pollution provided by the text file [ug/m^3]
    :param days: Number of days the year has, whether it's a leap year or not
    :return:
    """

    "Variable's initialization"
    # Arrays made for sorting the data through months (and computing the median of each month)
    # Size of the arrays
    size = int(12 * len(data_month) / days)
    # Index of the location
    index = np.array([0] * size, dtype=int)
    # Longitude of the location
    lon = np.array([0] * size, dtype=float)
    # Latitude of the location
    lat = np.array([0] * size, dtype=float)
    # Month
    month = np.array([0] * size, dtype=int)
    # Monthly mean of the pollutant's concentration of each location [ug/m^3]
    pollution = np.array([0] * size, dtype=float)
    # Monthly iqr of the pollutant's concentration of each location [ug/m^3]
    pollution_iqr = np.array([0] * size, dtype=float)
    # Monthly Yule-Kendall index of the pollutant's concentration of each location [ug/m^3]
    pollution_yule_kendall = np.array([0] * size, dtype=float)
    # Monthly kurtosis of the pollutant's concentration of each location [ug/m^3]
    pollution_kurtosis = np.array([0] * size, dtype=float)
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
    # Sorted iqr of the pollution [ug/m^3]
    sorted_pollution_iqr = np.array([0] * size, dtype=float)
    # Sorted Yule-Kendall index of the pollution [ug/m^3]
    sorted_pollution_yule_kendall = np.array([0] * size, dtype=float)
    # Sorted kurtosis of the pollution [ug/m^3]
    sorted_pollution_kurtosis = np.array([0] * size, dtype=float)
    # We initialize the statistical variables to be computed
    # Median
    monthly_median = np.array([0] * 12, dtype=float)
    # Interquartile range
    monthly_iqr = np.array([0] * 12, dtype=float)
    # Yule-Kendall index
    monthly_yule_kendall = np.array([0] * 12, dtype=float)
    # Robust kurtosis
    monthly_robust_kurtosis = np.array([0] * 12, dtype=float)
    # Mean of the pollution for every location for each month [ug/m^3]
    statistical_pollution = np.array([0] * int(len(data_month) / days), dtype=float)

    "Sorting data through months and obtaining the median of each month"
    for i in range(0, int(len(data_index) / days)):
        # We separate the data for every location
        index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, m = \
            monthly_separation(index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall,
                               pollution_kurtosis, monthly_pollution, data_index, data_lon, data_lat, data_month,
                               data_pollutant, i, m, days)

    "Location statistical analysis"
    # We compute the statistical variables
    sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, sorted_pollution_iqr, \
        sorted_pollution_yule_kendall, sorted_pollution_kurtosis,  monthly_median, monthly_iqr, monthly_yule_kendall, \
        monthly_robust_kurtosis = \
        monthly_statistics(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, sorted_pollution_iqr,
                           sorted_pollution_yule_kendall, sorted_pollution_kurtosis, monthly_median,
                           monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, statistical_pollution,
                           index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis)

    return (sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, sorted_pollution_iqr,
            sorted_pollution_yule_kendall, sorted_pollution_kurtosis, monthly_median, monthly_iqr,
            monthly_yule_kendall, monthly_robust_kurtosis)


@numba.njit()
def monthly_separation(index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis,
                       monthly_pollution, data_index, data_lon, data_lat, data_month, data_pollutant, i, m, days):
    """
    This function returns the monthly mean of the pollutant's concentration for every given location, allowing us
    to later perform an statistical analysis of the location.
    :param index:
    :param lon:
    :param lat:
    :param month:
    :param pollution:
    :param pollution_iqr:
    :param pollution_yule_kendall:
    :param pollution_kurtosis:
    :param monthly_pollution:
    :param data_index: Index to identify each location (longitude and latitude)
    :param data_lon: Longitude
    :param data_lat: Latitude
    :param data_month: Month
    :param data_pollutant: Mean of the day and location of the concentration of the pollutant [ug/m^3]
    :param i:
    :param m:
    :param days:
    :return: annual_index, annual_lon, annual_lat, annual_month, annual_day, annual_pollutant, j
    """

    # We initialize the variables
    j = i * days
    # We separate each index according to it's spatial location
    k = 0
    # Index which counts the days passed in a year
    n = 0
    # Index which counts the days passed in a month
    x = 0
    # The condition becomes false when the year has finished
    condition = True

    while condition:
        for l in range(0, days - 1):
            monthly_pollution[x] = data_pollutant[l + j + n]
            k += 1
            x += 1
            # When the year or the month have finished, we stop the iteration
            if ((l + j + n + 1) % days) == 0 or data_month[l + j + n] < data_month[l + j + n + 1]:
                x = 0
                break

        # We append the index, longitude, latitude, month and median of the pollution of each month to the variables
        index[m] = data_index[l + j + n]
        lon[m] = data_lon[l + j + n]
        lat[m] = data_lat[l + j + n]
        month[m] = data_month[l + j + n]
        pollution[m] = round(np.nanmean(monthly_pollution), 4)
        pollution_iqr[m] = round((np.nanquantile(monthly_pollution, 0.75) - (np.nanquantile(monthly_pollution, 0.25))),
                                 4)
        pollution_yule_kendall[m] = \
            round(((np.nanquantile(monthly_pollution, 0.75) + np.nanquantile(monthly_pollution, 0.25) -
                   2 * np.nanmedian(monthly_pollution)) / pollution_iqr[m]), 4)
        pollution_kurtosis[m] = \
            round((pollution_iqr[m] / (2 * (np.nanquantile(monthly_pollution, 0.90) -
                                            np.nanquantile(monthly_pollution, 0.10)))), 4)

        # If the year has ended, we stop the while loop
        if data_month[l + n] == 12:
            condition = False
        # We count the days of the year which have passed
        n = n + k
        m += 1
        k = 0
        for z in range(0, len(monthly_pollution)):
            monthly_pollution[z] = np.nan

    return index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, m


def monthly_statistics(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution,
                       sorted_pollution_iqr, sorted_pollution_yule_kendall, sorted_pollution_kurtosis, monthly_median,
                       monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, statistical_pollution,
                       index, lon, lat, month, pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis):
    """
    This function sorts all the arrays gathered from month separation by month, and also computes the statistical
    variables for each pollution concentration per month for every location.
    :param sorted_index:
    :param sorted_lon:
    :param sorted_lat:
    :param sorted_month:
    :param sorted_pollution:
    :param sorted_pollution_iqr:
    :param sorted_pollution_yule_kendall:
    :param sorted_pollution_kurtosis:
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
    :param pollution_iqr:
    :param pollution_yule_kendall:
    :param pollution_kurtosis:
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
        for k in range(0, n):
            sorted_index[k + j] = index[12 * k + m]
            sorted_lon[k + j] = lon[12 * k + m]
            sorted_lat[k + j] = lat[12 * k + m]
            sorted_month[k + j] = month[12 * k + m]
            sorted_pollution[k + j] = pollution[12 * k + m]
            sorted_pollution_iqr[k + j] = pollution_iqr[12 * k + m]
            sorted_pollution_yule_kendall[k + j] = pollution_yule_kendall[12 * k + m]
            sorted_pollution_kurtosis[k + j] = pollution_kurtosis[12 * k + m]
            statistical_pollution[k] = pollution[12 * k + m]
            i += 1

        monthly_median[m] = round(np.median(statistical_pollution), 4)
        monthly_iqr[m] = round(np.quantile(statistical_pollution, 0.75) - np.quantile(statistical_pollution, 0.25), 4)
        monthly_yule_kendall[m] = \
            round((np.quantile(statistical_pollution, 0.75) + np.quantile(statistical_pollution, 0.25) -
                   2 * monthly_median[m]) / monthly_iqr[m], 4)
        monthly_robust_kurtosis[m] = round(monthly_iqr[m] / (2 * (np.quantile(statistical_pollution, 0.9) -
                                                                  np.quantile(statistical_pollution, 0.10))), 4)
        m += 1
        j += i
        i = 0

    return (sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, sorted_pollution_iqr,
            sorted_pollution_yule_kendall, sorted_pollution_kurtosis, monthly_median, monthly_iqr, monthly_yule_kendall,
            monthly_robust_kurtosis)
