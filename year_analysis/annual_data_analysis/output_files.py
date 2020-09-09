# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis,
                       determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient,
                       name, years):
    """
    This is the main function used to create files that contains information we may use for the statistical analysis,
    such as statistical variables or the efficiency coefficients.
    :param annual_median: Annual median of each pollutant concentration
    :param annual_iqr: Annual interquartile range of each pollutant concentration
    :param annual_yule_kendall: Annual Yule-Kendall index of each pollutant concentration
    :param annual_robust_kurtosis: Annual robust kurtosis of each pollutant concentration
    :param determination_coefficient: Determination coefficient r^2
    :param d_coefficient: Index of agreement d
    :param e_coefficient: Nash-Sutcliffe efficiency E
    :param d_mod_coefficient: Modified form of d
    :param e_mod_coefficient: Modified form of E
    :param name: Name of the pollutant we are analysing
    :param years: Year of the data we are analyzing
    :return:
    """

    # We get the username
    username = os.getlogin()

    # We write the output files
    statistics_output(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis, name, years, username)
    efficiency_output(determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient,
                      name, years, username)

    return


def statistics_output(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis, name, years, username):
    """
    Function that creates a .txt file with the statistical variables per year of a pollutant.
    :param annual_median: Annual median of each pollutant concentration
    :param annual_iqr: Annual interquartile range of each pollutant concentration
    :param annual_yule_kendall: Annual Yule-Kendall index of each pollutant concentration
    :param annual_robust_kurtosis: Annual robust kurtosis of each pollutant concentration
    :param name: Name of the pollutant we are analysing
    :param years: Year of the data we are analyzing
    :param username: Username
    :return:
    """

    # We generate the data frame to output
    df = pd.DataFrame({'Year': years, 'Median': annual_median, 'IQR': annual_iqr,
                       'Yule-Kendall index': annual_yule_kendall, 'Robust kurtosis': annual_robust_kurtosis})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\annual_%s_statistical_variables.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep='\t')

    return


def efficiency_output(determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient,
                      name, years, username):
    """
    Function that creates a .txt file with the efficiency coefficients per year of a pollutant.
    :param determination_coefficient: Determination coefficient r^2
    :param d_coefficient: Index of agreement d
    :param e_coefficient: Nash-Sutcliffe efficiency E
    :param d_mod_coefficient: Modified form of d
    :param e_mod_coefficient: Modified form of E
    :param name: Name of the pollutant we are analysing
    :param years: Year of the data we are analyzing
    :param username: Username
    :return:
    """

    # We generate the data frame to output
    df = pd.DataFrame({'Year': years, 'r^2': determination_coefficient, 'd': d_coefficient, 'e': e_coefficient,
                       'd_mod': d_mod_coefficient, 'e_mod': e_mod_coefficient})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\annual_%s_efficiency_coefficients.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep='\t')

    return
