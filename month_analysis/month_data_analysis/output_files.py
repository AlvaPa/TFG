# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, longitude, latitude,
                       monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year,
                       pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient):
    """
    This function performs the output to the previously computed statistical variables and the sorted data.
    After that, it closes the data opened at the beginning of the iteration
    :param pollution:
    :param longitude:
    :param latitude:
    :param monthly_median:
    :param monthly_iqr:
    :param monthly_yule_kendall:
    :param monthly_robust_kurtosis:
    :param name:
    :param year:
    :return:
    """

    # We get the username
    username = os.getlogin()

    output_sorted_data(pollution, longitude, latitude, name, year, username)
    output_sorted_iqr(pollution_iqr, longitude, latitude, name, year, username)
    output_sorted_yule_kendall(pollution_yule_kendall, longitude, latitude, name, year, username)
    output_sorted_kurtosis(pollution_kurtosis, longitude, latitude, name, year, username)
    statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year, username)
    efficiency_output(pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name,
                      year, username)

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


def output_sorted_iqr(pollution_iqr, longitude, latitude, name, year, username):
    """"""

    # We establish the chunk size
    chunk_size = 10 ** 6

    # We generate the data frame to output for each month
    for i in range(0, 12):
        df = pd.DataFrame({'lon': longitude[i, ::], 'lat': latitude[i, ::], '%s' % name: pollution_iqr[i, ::]})
        # We generate the file
        absolute_path = os.path.abspath(os.path.join(r'C:\Users\%s\Desktop\practicas_alvaro\output_data' % username,
                                                     'sorted_%s_%s_%s_iqr.txt' % (name, year, str(i + 1))))
        with open(absolute_path, 'w+') as file:
            # We write the file
            df.to_csv(file, index=False, chunksize=chunk_size, sep=',')

    return


def output_sorted_yule_kendall(pollution_yule_kendall, longitude, latitude, name, year, username):
    """"""

    # We establish the chunk size
    chunk_size = 10 ** 6

    # We generate the data frame to output for each month
    for i in range(0, 12):
        df = pd.DataFrame({'lon': longitude[i, ::], 'lat': latitude[i, ::], '%s' % name: pollution_yule_kendall[i, ::]})
        # We generate the file
        absolute_path = os.path.abspath(os.path.join(r'C:\Users\%s\Desktop\practicas_alvaro\output_data' % username,
                                                     'sorted_%s_%s_%s_yule_kendall.txt' % (name, year, str(i + 1))))
        with open(absolute_path, 'w+') as file:
            # We write the file
            df.to_csv(file, index=False, chunksize=chunk_size, sep=',')

    return


def output_sorted_kurtosis(pollution_kurtosis, longitude, latitude, name, year, username):
    """"""

    # We establish the chunk size
    chunk_size = 10 ** 6

    # We generate the data frame to output for each month
    for i in range(0, 12):
        df = pd.DataFrame({'lon': longitude[i, ::], 'lat': latitude[i, ::], '%s' % name: pollution_kurtosis[i, ::]})
        # We generate the file
        absolute_path = os.path.abspath(os.path.join(r'C:\Users\%s\Desktop\practicas_alvaro\output_data' % username,
                                                     'sorted_%s_%s_%s_kurtosis.txt' % (name, year, str(i + 1))))
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


def efficiency_output(pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name,
                      year, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'r': pearson_coefficient, 'd': d_coefficient, 'e': e_coefficient, 'dmod': d_mod_coefficient,
                       'emod': e_mod_coefficient})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\%s_%s_efficiency_coefficients.txt' % (username, name,
                                                                                                       year),
              'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep='\t')

    return
