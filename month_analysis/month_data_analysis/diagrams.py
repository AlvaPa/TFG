# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import os
from constants import *


def diagrams_representation(sorted_pollution, sorted_lon, sorted_lat, name, year):
    """
    Main function of the script. Its purpose is sort the pollutant's concentration by month and, after that, plot the
    violin plots of the monthly pollution in a single graphic.
    :param sorted_pollution: Sorted mean monthly pollution
    :param sorted_lon: Sorted longitude
    :param sorted_lat: Sorted latitude
    :param name: Pollutant's name
    :param year: Year we are analysing
    :return: pollution, longitude, latitude, dictionary
    """

    # We get the username
    username = os.getlogin()

    # We sort the pollution data, the longitude and the latitude
    pollution, longitude, latitude, dictionary = sorting_data(sorted_pollution, sorted_lon, sorted_lat)

    # We compute the medians, iqr and whiskers. We also compute the positions where each component goes.
    lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians, positions = \
        boxplots_parameters(pollution)

    # We make the boxplots of the pollutants
    boxplot(dictionary, lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians,
            positions, name, year, username)

    return pollution, longitude, latitude


def sorting_data(sorted_pollution, sorted_lon, sorted_lat):
    """
    This function sorts the data according to the month (all the pollution's concentration of each location January
    are in the first place, and so on).
    :param sorted_pollution: Sorted mean monthly pollution
    :param sorted_lon: Sorted longitude
    :param sorted_lat: Sorted latitude
    :return: pollution, longitude, latitude, dictionary
    """

    # Initialize array for months and dictionary, also the longitude and latitude
    dictionary = {}
    # Pollution for the output
    pollution = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    # Longitude
    longitude = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    # Latitude
    latitude = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    # Parameter to count each location that has been plotted
    k = 0
    # Parameter to separate through months
    n = 0

    # We go through the data to sort it by month. For each month, we separate each location's pollution per month and
    # assign it to different rows of the array.
    for i in range(0, 12):
        for j in range(0, int(len(sorted_pollution) / 12)):
            pollution[i, j] = sorted_pollution[j + n]
            longitude[i, j] = sorted_lon[j + n]
            latitude[i, j] = sorted_lat[j + n]
            k += 1

        n += k
        k = 0
        # We add the month's pollution to the dictionary to plot all the months later
        dictionary['month_%s' % str(i + 1)] = pollution[i, ::]

    return pollution, longitude, latitude, dictionary


def boxplots_parameters(pollution):
    """
    This function computes all the elements necessary to plot the violin plot: the superior and inferior quartiles, the
    medians and the upper and lower adjacent values. We also compute the positions where each violin plot will be
    represented (in order to depict all the violin plots in a single graphic).
    :param pollution: Sorted mean monthly pollution by month
    :return: lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians, positions
    """

    # We initialize the adjacent values
    upper_adjacent_value = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    lower_adjacent_value = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    # We initialize the superior quartile, the inferior quartile and the median
    superior_quartile = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    inferior_quartile = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    medians = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    # We compute the positions
    positions = np.arange(1, len(medians) + 1)

    for i in range(0, len(pollution)):
        # We compute the superior and inferior quartiles
        sorted_data = np.sort(pollution[i])
        superior_quartile[i] = np.quantile(sorted_data, 0.75)
        inferior_quartile[i] = np.quantile(sorted_data, 0.25)
        medians[i] = np.median(sorted_data)

        # We compute the upper and lower adjacent values
        upper_adjacent_value[i] = superior_quartile[i] + (superior_quartile[i] - inferior_quartile[i]) * 1.5
        upper_adjacent_value[i] = np.clip(upper_adjacent_value[i], superior_quartile[i], sorted_data[-1])

        lower_adjacent_value[i] = inferior_quartile[i] - (superior_quartile[i] - inferior_quartile[i]) * 1.5
        lower_adjacent_value[i] = np.clip(lower_adjacent_value[i], sorted_data[0], inferior_quartile[i])

    return lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians, positions


def boxplot(dictionary, lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians,
            positions, name, year, username):
    """
    This function represents the violin plots of each month of the pollution's concentration in each location in a
    single image.
    :param dictionary: Dictionary which holds all the mean monthly concentrations in different keys.
    :param lower_adjacent_value: Lower adjacent value
    :param upper_adjacent_value: Upper adjacent value
    :param superior_quartile: Superior quartile
    :param inferior_quartile: Inferior quartile
    :param medians: Medians
    :param positions: Position of each violin plot
    :param name: Pollutant's name
    :param year: Year we are analysing
    :param username: Username
    :return:
    """

    # We plot the box and whiskers plot for the whole year

    # Parameters
    fig = plt.figure(12, figsize=(18, 12))
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                  alpha=0.5)
    ax.set_axisbelow(True)
    # We select the range of plot
    if name == no2:
        ax.set_ylim(10, 100)
        ax.yaxis.set_ticks(np.arange(10, 100, 10))
    elif name == ozone:
        ax.set_ylim(30, 100)
        ax.yaxis.set_ticks(np.arange(30, 100, 10))
    elif name == pm_10:
        ax.set_ylim(7.5, 27.5)
        ax.yaxis.set_ticks(np.arange(7.5, 27.5, 2.5))
    else:
        ax.set_ylim(0, 40)
        ax.yaxis.set_ticks(np.arange(0, 40, 5))
    # We plot the violin plot
    parts = ax.violinplot(dictionary.values(), showmedians=False, showextrema=False)
    for pc in parts['bodies']:
        pc.set_facecolor('#D43F3A')
        pc.set_edgecolor('blue')
        pc.set_alpha(1)

    # We change the name of the labels in the x axis
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_ylabel(r'Concentration ($\frac{{\mu}g}{m^{3}}$)', size=50)
    ax.set_xlabel('Months', size=50)
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.tick_params(axis='both', which='minor', labelsize=36)
    ax.tick_params(axis='x', rotation=45)

    # Medians
    ax.scatter(positions, medians, marker='o', color='white', s=30, zorder=3)
    # IQR
    ax.vlines(positions, inferior_quartile, superior_quartile, color='k', linestyle='-', lw=5)
    # Whiskers
    ax.vlines(positions, lower_adjacent_value, upper_adjacent_value, color='k', linestyle='-', lw=1)

    # We save the file
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_paper.tiff'
                % (username, name, year), bbox_inches='tight', dpi=300)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_paper.png'
                % (username, name, year), bbox_inches='tight', dpi=90)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_paper.jpg'
                % (username, name, year), bbox_inches='tight', quality=10)
    # We close the figure
    plt.close(12)

    return
