# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(pollution, longitude, latitude, monthly_median, monthly_iqr, monthly_yule_kendall,
                       monthly_robust_kurtosis, name, year):
    """
    This function performs the output to the previously computed statistical variables and the sorted data.
    After that, it closes the data opened at the beginning of the iteration
    :param pollution: Monthly pollution sorted by month
    :param longitude: Longitude sorted by month
    :param latitude: Latitude sorted by month
    :param monthly_median: Median of the monthly pollution
    :param monthly_iqr: Interquartile range of the monthly pollution
    :param monthly_yule_kendall: Yule-Kendall index of the monthly pollution
    :param monthly_robust_kurtosis: Robust Kurtosis of the monthly pollution
    :param name: Pollutant's name
    :param year: Year we are analysing
    :return:
    """

    # We get the username
    username = os.getlogin()

    output_sorted_data(pollution, longitude, latitude, name, year, username)
    statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year, username)

    return


def output_sorted_data(pollution, longitude, latitude, name, year, username):
    """"""

    # We establish the chunk size
    chunk_size = 10 ** 6

    # We generate the data frame to output for each month
    for i in range(0, 12):
        df = pd.DataFrame({'lon': longitude[i, ::], 'lat': latitude[i, ::], '%s' % name: pollution[i, ::]})
        # We generate the file
        absolute_path = os.path.abspath(os.path.join(r'C:\Users\%s\Desktop\practicas_alvaro\output_data' % username,
                                                     'sorted_%s_%s_%s_data.txt' % (name, year, str(i + 1))))
        with open(absolute_path, 'w+') as file:
            # We write the file
            df.to_csv(file, index=False, chunksize=chunk_size, sep=',')

    return


def statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year,
                      username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'Median': monthly_median, 'IQR': monthly_iqr, 'Yule-Kendall index': monthly_yule_kendall,
                       'Robust kurtosis': monthly_robust_kurtosis})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\%s_%s_statistical_variables.txt' % (username, name,
                                                                                                     year),
              'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep='\t')

    return
