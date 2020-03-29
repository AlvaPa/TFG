# encoding utf-8 #

import pandas as pd
import os


def output_and_closing(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis, pearson_coefficient,
                       d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name, years):
    """"""

    # We get the username
    username = os.getlogin()

    # We write the output files
    statistics_output(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis, name, years, username)
    efficiency_output(pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name,
                      years, username)

    return


def statistics_output(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis, name, years, username):
    """"""

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


def efficiency_output(pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name,
                      years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'Year': years, 'r': pearson_coefficient, 'd': d_coefficient, 'e': e_coefficient,
                       'dmod': d_mod_coefficient, 'emod': e_mod_coefficient})
    # We establish the chunk size
    chunk_size = 10 ** 6
    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\annual_%s_efficiency_coefficients.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, chunksize=chunk_size, sep='\t')

    return
