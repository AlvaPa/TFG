# encoding utf-8 #

import pandas as pd
import numpy as np
import os
import sys


def read(root, name, year, month):
    """"""

    # We generate the file's name for the pollutant and year
    file_name = 'sorted_%s_%s_%s_data.txt' % (name, year, month)
    # We generate the absolute path
    absolute_path = os.path.abspath(os.path.join(root, file_name))
    # We open the files and assign the variables
    lon, lat, pollution = file_opening(absolute_path, name)

    return lon, lat, pollution


def path_finder():
    """
    Function designed to find the path of the file we want to analyze. With this we can use the absolute path for
    every user without having to change the code.
    :return: root
    """

    # We generate the value which contains the name of the file we're going to search
    file_name = 'sorted_no2_2007_1_data.txt'
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
    :return: index, lon, lat, month, day, pollutant
    """

    # We initialize the arrays to contain the file's data
    data_lon = np.array([], dtype=float)
    data_lat = np.array([], dtype=float)
    data_pollution = np.array([], dtype=float)

    # We start reading the file. Since it's so big, chunk of data are loaded at a time
    df = pd.read_csv(absolute_path, sep=",", dtype={'lon': float, 'lat': float, '%s' % name: float}, low_memory=False,
                     compression=None)
    data_lon = np.append(data_lon, np.array(df['lon'].values.tolist(), dtype=float))
    data_lat = np.append(data_lat, np.array(df['lat'].values.tolist(), dtype=float))
    data_pollution = np.append(data_pollution, np.array(df['%s' % name].values.tolist(), dtype=float))

    return data_lon, data_lat, data_pollution
