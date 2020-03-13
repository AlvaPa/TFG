# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(pollution, longitude, latitude, monthly_median,
                       monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year, r, e, d, e_mod, d_mod):
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

    output_sorted_data(pollution, longitude, latitude, name, year)
    statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year)
    coefficients_output(r, e, d, e_mod, d_mod, name, year)

    return


def output_sorted_data(pollution, longitude, latitude, name, year):
    """"""

    # We establish the chunk size
    chunk_size = 10 ** 6

    # We generate the data frame to output for each month
    for i in range(0, 12):
        df = pd.DataFrame({'lon': longitude[i, ::], 'lat': latitude[i, ::], '%s' % name: pollution[i, ::]})
        # We generate the file
        absolute_path = os.path.abspath(os.path.join(r'C:\Users\FA\Desktop\practicas_alvaro\output_data',
                                                     'sorted_%s_%s_%s_data.txt' % (name, year, str(i + 1))))
        with open(absolute_path, 'w+') as file:
            # We write the file
            df.to_csv(file, index=False, chunksize=chunk_size, sep=',')

    return


def statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'Median': monthly_median, 'IQR': monthly_iqr, 'Yule-Kendall index': monthly_yule_kendall,
                       'Robust kurtosis': monthly_robust_kurtosis})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\FA\Desktop\practicas_alvaro\output_data\%s_%s_statistical_variables.txt' % (name, year),
              'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep=',')

    return


def coefficients_output(r, e, d, e_mod, d_mod, name, year):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'r': r, 'd': d, 'e': e, 'd_mod': d_mod, 'e_mod': e_mod})
    # We generate the file
    absolute_path = os.path.abspath(os.path.join(r'C:\Users\FA\Desktop\practicas_alvaro\output_data',
                                                 'efficiency_coefficients_%s_%s.txt' % (name, year)))
    with open(absolute_path, 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep=',')
