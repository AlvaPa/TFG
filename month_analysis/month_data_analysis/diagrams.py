# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import os
from constants import *


def diagrams_representation(sorted_pollution, sorted_pollution_iqr, sorted_pollution_yule_kendall,
                            sorted_pollution_kurtosis, sorted_lon, sorted_lat, name, big_name, year):
    """"""

    # We get the username
    username = os.getlogin()

    # We make the boxplots of the pollutants
    pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, pollution_histogram, longitude, latitude = \
        boxplot(sorted_pollution, sorted_pollution_iqr, sorted_pollution_yule_kendall, sorted_pollution_kurtosis,
                sorted_lon, sorted_lat, name, big_name, year, username)

    # We compute the kernel density smoothing to plot it next to the histograms
    # We initialize some parameters
    h = np.array([0] * 12, dtype=float)
    quadratic_function = np.array([[0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                   [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                   [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                   [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                   [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                                   [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::])], dtype=float)
    # We compute the quadratic function
    # quadratic_function = quadratic_kernel(pollution_histogram, h, quadratic_function)

    # We plot the histogram and the kernel density smoothing
    # bar_values = histogram(pollution_histogram, name, big_name, year, quadratic_function, username)

    # We initialize the coefficients to determine the efficiency of the parametric curves
    pearson_coefficient = np.array([0] * 12, dtype=float)
    d_coefficient = np.array([0] * 12, dtype=float)
    e_coefficient = np.array([0] * 12, dtype=float)
    d_mod_coefficient = np.array([0] * 12, dtype=float)
    e_mod_coefficient = np.array([0] * 12, dtype=float)

    return (pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, longitude, latitude,
            pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient)


def boxplot(sorted_pollution, sorted_pollution_iqr, sorted_pollution_yule_kendall, sorted_pollution_kurtosis,
            sorted_lon, sorted_lat, name, big_name, year, username):
    """
    This function represents the box and whiskers plot for each month of the pollution's concentration in each location.
    Then it represents all the twelve box and whiskers plot in a single graphic to compare.
    :param sorted_pollution:
    :param sorted_pollution_iqr:
    :param sorted_pollution_yule_kendall:
    :param sorted_pollution_kurtosis:
    :param sorted_lon:
    :param sorted_lat:
    :param name:
    :param big_name:
    :param year:
    :param username:
    :return:
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
    pollution_iqr = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    pollution_yule_kendall = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    pollution_kurtosis = \
        np.array([[0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12),
                  [0] * int(len(sorted_pollution) / 12), [0] * int(len(sorted_pollution) / 12)], dtype=float)
    # Pollution for the histogram
    pollution_histogram = \
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
            pollution_iqr[i, j] = sorted_pollution_iqr[j + n]
            pollution_yule_kendall[i, j] = sorted_pollution_yule_kendall[j + n]
            pollution_kurtosis[i, j] = sorted_pollution_kurtosis[j + n]
            pollution_histogram[i, j] = sorted_pollution[j + n]
            longitude[i, j] = sorted_lon[j + n]
            latitude[i, j] = sorted_lat[j + n]
            k += 1

        n += k
        k = 0
        # We add the month's pollution to the dictionary to plot all the months later
        dictionary['month_%s' % str(i + 1)] = pollution_histogram[i, ::]

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
        ax.set_ylim(0, 100)
        ax.yaxis.set_ticks(np.arange(0, 100, 10))
    elif name == ozone:
        ax.set_ylim(0, 140)
        ax.yaxis.set_ticks(np.arange(0, 140, 10))
    elif name == pm_10:
        ax.set_ylim(0, 45)
        ax.yaxis.set_ticks(np.arange(0, 45, 5))
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
    labels_spanish = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                      'Noviembre', 'Diciembre']
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels_spanish)
    ax.set_ylabel(r'Concentración ($\frac{{\mu}g}{m^{3}}$)', size=50)
    ax.set_xlabel('Meses', size=50)
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.tick_params(axis='both', which='minor', labelsize=36)
    ax.tick_params(axis='x', rotation=45)

    # We compute the medians, iqr and whiskers
    lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians, upper_extrema, \
    lower_extrema = boxplots_parameters(pollution)
    positions = np.arange(1, len(medians) + 1)
    positions_extrema = np.array([[1] * len(pollution[0]), [2] * len(pollution[0]), [3] * len(pollution[0]),
                                  [4] * len(pollution[0]), [5] * len(pollution[0]), [6] * len(pollution[0]),
                                  [7] * len(pollution[0]), [8] * len(pollution[0]), [9] * len(pollution[0]),
                                  [10] * len(pollution[0]), [11] * len(pollution[0]), [12] * len(pollution[0])],
                                 dtype=int)
    # Medians
    ax.scatter(positions, medians, marker='o', color='white', s=30, zorder=3)
    # IQR
    ax.vlines(positions, inferior_quartile, superior_quartile, color='k', linestyle='-', lw=5)
    # Whiskers
    ax.vlines(positions, lower_adjacent_value, upper_adjacent_value, color='k', linestyle='-', lw=1)
    # Extrema
    # ax.scatter(positions_extrema, upper_extrema, marker='.', color='green', s=0.005, zorder=3)
    # ax.scatter(positions_extrema, lower_extrema, marker='.', color='green', s=0.005, zorder=3)

    # We save the file
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_spanish.tiff'
                % (username, name, year), bbox_inches='tight', dpi=300)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_spanish.png'
                % (username, name, year), bbox_inches='tight', dpi=90)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\monthly\%s_%s_boxplot_definitive_spanish.jpg'
                % (username, name, year), bbox_inches='tight', quality=10)
    # We close the figure
    plt.close(12)

    return (pollution, pollution_iqr, pollution_yule_kendall, pollution_kurtosis, pollution_histogram, longitude,
            latitude)


def boxplots_parameters(pollution):
    """"""

    # We initialize the adjacent values
    upper_adjacent_value = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    lower_adjacent_value = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    # We initialize the superior quartile, the inferior quartile and the median
    superior_quartile = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    inferior_quartile = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    medians = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    # We initialize the inferior and superior extreme values
    lower_extrema = np.array([[0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0])],
                             dtype=float)

    upper_extrema = np.array([[0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0]),
                              [0] * len(pollution[0]), [0] * len(pollution[0]), [0] * len(pollution[0])],
                             dtype=float)

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

        # We compute the upper and lower extrema
        upper_extrema[i, ::] = sorted_data
        upper_extrema[i] = np.clip(upper_extrema[i], upper_adjacent_value[i], sorted_data[-1])

        lower_extrema[i] = sorted_data
        lower_extrema[i] = np.clip(lower_extrema[i], sorted_data[0], lower_adjacent_value[i])

    return (lower_adjacent_value, upper_adjacent_value, superior_quartile, inferior_quartile, medians, upper_extrema,
            lower_extrema)


def month_selector(i):
    """"""

    if i == 0:
        month = 'January'
    elif i == 1:
        month = 'February'
    elif i == 2:
        month = 'March'
    elif i == 3:
        month = 'April'
    elif i == 4:
        month = 'May'
    elif i == 5:
        month = 'June'
    elif i == 6:
        month = 'July'
    elif i == 7:
        month = 'August'
    elif i == 8:
        month = 'September'
    elif i == 9:
        month = 'October'
    elif i == 10:
        month = 'November'
    else:
        month = 'December'

    return month
