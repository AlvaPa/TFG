# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median,
                       monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year):
    """
    This function performs the output to the previously computed statistical variables and the sorted data.
    After that, it closes the data opened at the beginning of the iteration
    :param sorted_index:
    :param sorted_lon:
    :param sorted_lat:
    :param sorted_month:
    :param sorted_pollution:
    :param monthly_median:
    :param monthly_iqr:
    :param monthly_yule_kendall:
    :param monthly_robust_kurtosis:
    :param name:
    :param year:
    :return:
    """

    output_sorted_data(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, name, year)
    statistics_output(monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis, name, year)

    return


def output_sorted_data(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, name, year):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'index': sorted_index, 'lon': sorted_lon, 'lat': sorted_lat, 'month': sorted_month,
                       '%s' % name: sorted_pollution})
    # We establish the chunk size
    chunk_size = 10 ** 6
    # We generate the file
    absolute_path = os.path.abspath(os.path.join(r'C:\Users\FA\Desktop\practicas_alvaro\output_data',
                                                 'sorted_%s_%s_data.txt' % (name, year)))
    with open(r'C:\Users\FA\Desktop\practicas_alvaro\output_data\sorted_%s_%s_data.txt' % (name, year), 'w+') \
            as file:
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
