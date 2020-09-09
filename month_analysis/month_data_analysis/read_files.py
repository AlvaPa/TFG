# encoding utf-8 #

import pandas as pd
import numpy as np
import os
import sys


def read(root, name, year):
    """
    Main function of this script, where all the other functions are called to read the files necessary to perform the
    statistical analysis.
    :return: data_index, data_lon, data_lat, data_month, data_pollutant
    """
    # We generate the file's name for the pollutant and year
    file_name = 'surface_%s_%s.txt.gz' % (year, name)
    # We generate the absolute path
    absolute_path = os.path.abspath(os.path.join(root, file_name))
    # We open the file and assign the variables
    data_index, data_lon, data_lat, data_month, data_pollutant = file_opening(absolute_path, name)

    return data_index, data_lon, data_lat, data_month, data_pollutant


def path_finder():
    """
    Function designed to find the path of the file we want to analyze. With this we can use the absolute path for
    every user without having to change the code.
    :return: root
    """

    # We generate the value which contains the name of the file we're going to search
    file_name = 'surface_2007_no2.txt.gz'
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
    :return: data_index, data_lon, data_lat, data_month, data_pollutant
    """

    # We specify the size of the chunk of data loaded at one time
    chunk_size = 10 ** 6

    # We initialize the arrays to contain the file's data
    data_index = np.array([], dtype=int)
    data_lon = np.array([], dtype=float)
    data_lat = np.array([], dtype=float)
    data_month = np.array([], dtype=int)
    data_pollutant = np.array([], dtype=float)

    # We start reading the file. Since it's so big, chunk of data are loaded at a time
    for chunk in pd.read_csv(absolute_path, sep=" ", compression='gzip',
                             dtype={'index': int, 'lon': float, 'lat': float, 'year': int, 'month': int, 'day': int,
                                    'aqum': float, '%s' % name: float, 'sd': float}, low_memory=False,
                             chunksize=chunk_size):
        data_index = np.append(data_index, np.array(chunk['index'].tolist(), dtype=int))
        data_lon = np.append(data_lon, np.array(chunk['lon'].tolist(), dtype=float))
        data_lat = np.append(data_lat, np.array(chunk['lat'].tolist(), dtype=float))
        data_month = np.append(data_month, np.array(chunk['month'].tolist(), dtype=int))
        data_pollutant = np.append(data_pollutant, np.array(chunk['%s' % name].tolist(), dtype=float))

    return data_index, data_lon, data_lat, data_month, data_pollutant
