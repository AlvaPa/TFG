# encoding utf-8 #

import pandas as pd
import numpy as np
import os
import sys
from constants import *


def read(root, name):
    """"""
    # We initialize the variables containing the pollutant's names and years
    years = [first_year, second_year, third_year, fourth_year, fifth_year]

    # We initialize the arrays to contain the file's data
    r_coefficient = np.array([], dtype=int)
    d_coefficient = np.array([], dtype=float)
    e_coefficient = np.array([], dtype=float)
    d_mod_coefficient = np.array([], dtype=int)
    e_mod_coefficient = np.array([], dtype=float)

    # We start the iterations for every year
    for i in range(0, 5):
        # We select the current year
        year = years[i]

        # We generate the file's name for the pollutant and year
        file_name = '%s_%s_efficiency_coefficients.txt' % (name, year)

        # We generate the absolute path
        absolute_path = os.path.abspath(os.path.join(root, file_name))

        r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
            file_opening(absolute_path, r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient,
                         e_mod_coefficient)

    return r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient


def path_finder():
    """
    Function designed to find the path of the file we want to analyze. With this we can use the absolute path for
    every user without having to change the code.
    :return: root
    """

    # We generate the value which contains the name of the file we're going to search
    file_name = 'no2_2007_efficiency_coefficients.txt'
    # We search the user's name home directory
    home_directory = os.path.expanduser('~')
    # We join the directory to the desktop
    home_directory = os.path.abspath(os.path.join(home_directory, 'Desktop'))
    # We search across all directories in Users a file's name equal to the one we have designed. Once it founds it,
    # it returns its absolute path.
    for root, dirs, files in os.walk(home_directory):
        for name in files:
            if name == file_name:
                return root
    # In case it had not found it, the code stops
    sys.exit('The file does not exist.')


def file_opening(absolute_path, r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient,
                 e_mod_coefficient):
    """"""

    # We start reading the file. Since it's so big, chunk of data are loaded at a time
    df = pd.read_csv(absolute_path, sep="\t", dtype={'r': float, 'd': float, 'e': float, 'dmod': float,
                                                    'emod': float}, low_memory=False)

    r_coefficient = np.append(r_coefficient, np.array(df['r'].tolist(), dtype=float))
    d_coefficient = np.append(d_coefficient, np.array(df['d'].tolist(), dtype=float))
    e_coefficient = np.append(e_coefficient, np.array(df['e'].tolist(), dtype=float))
    d_mod_coefficient = np.append(d_mod_coefficient, np.array(df['dmod'].tolist(), dtype=float))
    e_mod_coefficient = np.append(e_mod_coefficient, np.array(df['emod'].tolist(), dtype=float))

    return r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
