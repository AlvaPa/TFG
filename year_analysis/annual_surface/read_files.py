# encoding utf-8 #

import pandas as pd
import numpy as np
import os
import sys


def read(root, name, year):
    """
    Main function of this script, where all the other functions are called to read the files necessary to perform the
    statistical analysis.
    :return:
    """
    # We generate the file's name for the pollutant and year
    file_name = 'grid_1km_annual_%s_%s.txt' % (name, year)
    # We generate the absolute path
    absolute_path = os.path.abspath(os.path.join(root, file_name))
    # We open the file and assign the variables
    lon, lat, pollution = file_opening(absolute_path, name)

    return lon, lat, pollution


def path_finder():
    """
    Function designed to find the path of the file we want to analyze. With this we can use the absolute path for
    every user without having to change the code.
    :return: root
    """

    # We generate the value which contains the name of the file we're going to search
    file_name = 'grid_1km_annual_no2_2007.txt'
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


def file_opening(absolute_path, name):
    """
    Function designed to open the files with the stored data. It opens all the data necessary to perform the statistical
    analysis.
    :param absolute_path: Absolute path of the file to be opened.
    :param name: Pollutant's name
    :return: lon, lat, pollution, standard_deviation
    """

    # We initialize the arrays to contain the file's data
    lon = np.array([], dtype=float)
    lat = np.array([], dtype=float)
    pollution = np.array([], dtype=float)

    # We start reading the file. Since it's so big, chunk of data are loaded at a time
    df = pd.read_csv(absolute_path, sep=" ",
                     dtype={'index': int, 'lon': float, 'lat': float, 'year': int, 'aqum': float,
                            '%s' % name: float, 'sd': float, '95low': float, '95up': float}, low_memory=False)
    lon = np.append(lon, np.array(df['lon'].tolist(), dtype=float))
    lat = np.append(lat, np.array(df['lat'].tolist(), dtype=float))
    pollution = np.append(pollution, np.array(df['%s' % name].tolist(), dtype=float))

    return lon, lat, pollution
