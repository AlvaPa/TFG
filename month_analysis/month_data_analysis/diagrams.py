# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import numba
import os
from constants import *


def diagrams_representation(sorted_pollution, sorted_lon, sorted_lat, name, big_name, year):
    """"""

    # We get the username
    username = os.getlogin()

    # We make the boxplots of the pollutants
    pollution, pollution_histogram, longitude, latitude = boxplot(sorted_pollution, sorted_lon, sorted_lat, name,
                                                                  big_name, year, username)

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
    quadratic_function = quadratic_kernel(pollution_histogram, h, quadratic_function)

    # We plot the histogram and the kernel density smoothing
    bar_values = histogram(pollution_histogram, name, big_name, year, quadratic_function, username)
    # We initialize the coefficients to determine the efficiency of the parametric curves
    pearson_coefficient = np.array([0] * 12, dtype=float)
    d_coefficient = np.array([0] * 12, dtype=float)
    e_coefficient = np.array([0] * 12, dtype=float)
    d_mod_coefficient = np.array([0] * 12, dtype=float)
    e_mod_coefficient = np.array([0] * 12, dtype=float)

    # We compute the efficiency coefficients
    pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
        efficiency_criteria(bar_values, quadratic_function, pearson_coefficient, d_coefficient, e_coefficient,
                            d_mod_coefficient, e_mod_coefficient)

    return (pollution, longitude, latitude, pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient,
            e_mod_coefficient)


def boxplot(sorted_pollution, sorted_lon, sorted_lat, name, big_name, year, username):
    """
    This function represents the box and whiskers plot for each month of the pollution's concentration in each location.
    Then it represents all the twelve box and whiskers plot in a single graphic to compare.
    :param sorted_pollution:
    :param sorted_lon
    :param sorted_lat
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
    ax.set_title('Location boxplots of the concentration of %s during the year %s' % (big_name, year))
    ax.set_xticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                        'October', 'November', 'December'])
    ax.set_ylabel(r'Concentration ($\frac{{\mu}g}{m^{3}}$)')
    ax.set_xlabel('Months')
    # We select the range of plot
    if name == no2:
        ax.set_ylim(0, 100)
    elif name == ozone:
        ax.set_ylim(0, 140)
    elif name == pm_10:
        ax.set_ylim(0, 35)
    else:
        ax.set_ylim(0, 40)
    # We plot the box and whiskers
    ax.boxplot(dictionary.values())
    # We save the file
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\%s_%s_boxplot_definitive.tiff'
                % (username, name, year), bbox_inches='tight', dpi=300)
    # We close the figure
    plt.close(12)

    return pollution, pollution_histogram, longitude, latitude


def histogram(pollution, name, big_name, year, quadratic_function, username):
    """
    This function represents the histogram and the parametric plot of the probabilites of the concentrations in the same
    diagram per month
    :param pollution:
    :param name:
    :param big_name:
    :param year:
    :param quadratic_function:
    :param username:
    :return: bar_values
    """
    # We initialize the array which will contain the probability of the bars of the histogram
    bar_values = np.array([[0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                           [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                           [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                           [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                           [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::]),
                           [0] * len(pollution[0, ::]), [0] * len(pollution[0, ::])], dtype=float)

    for i in range(0, 12):
        # We compute the width of the bins
        n_bins = 130
        pollution_range = np.max(pollution[i, ::]) - np.min(pollution[i, ::])
        width = float(pollution_range / (n_bins + 1))
        # We start plotting the histogram
        month = month_selector(i)
        fig = plt.figure(i, figsize=(9, 6))
        ax = fig.add_subplot(111)
        ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)
        ax.set_axisbelow(True)
        ax.set_title('Location histogram and Epanechnikov density smoothing of the concentration of %s in %s %s'
                     % (big_name, month, year))
        ax.set_xlabel(r'Concentration ($\frac{{\mu}g}{m^{3}}$)')
        ax.set_ylabel('Probability density')
        output = ax.hist(pollution[i, ::], bins=n_bins, density=True)
        ax.plot(pollution[i, ::], quadratic_function[i, ::], '--', lw=1.5)
        ax.text(0.7, 0.95, r'Bin width = %f $\frac{{\mu}g}{m^{3}}$' % width, transform=ax.transAxes)
        fig.tight_layout()
        plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\histograms\%s_%s_%s_histograms.tiff'
                    % (username, name, year, str(i + 1)), bbox_inches='tight', dpi=300)
        # We assign the bar probability values
        # We convert the output to array
        n = np.asarray(output[0])
        for j in range(0, len(n)):
            for k in range(0, 1164):
                m = j * 1164 + k
                if m >= len(bar_values[0]):
                    break
                bar_values[i, m] = n[j]
        plt.close(i)

    return bar_values


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


@numba.jit(nopython=True)
def quadratic_kernel(pollution, h, quadratic_function):
    """"""

    # We start computing the functions
    k_t = 0
    for i in range(0, 12):
        # Standard deviation
        s = np.std(pollution[i, ::])
        # Number of elements
        n = len(pollution[i, ::])
        # Bandwidth
        h[i] = 0.9 * s / (n ** 0.2)
        divisor = 1.0 / h[i]
        pollution[i, ::] = np.sort(pollution[i, ::])
        for j in range(0, n):
            for k in range(0, n):
                t = (pollution[i, j] - pollution[i, k]) * divisor
                if abs(t) < 1.0 and j != k:
                    k_t += 0.75 * (1 - t ** 2)
                if t > 1.0:
                    continue
            constant = h[i] * n
            quadratic_function[i, j] = k_t / constant
            k_t = 0

    return quadratic_function


def efficiency_criteria(bar_values, quadratic_function, pearson_coefficient, d_coefficient, e_coefficient,
                        d_mod_coefficient, e_mod_coefficient):
    """"""

    # We perform the calculations
    for i in range(0, 12):
        # We initialize some variables to perform to calculations
        num_r = 0.0
        den_r_poll = 0.0
        den_r_quar = 0.0
        num_d = 0.0
        den_d = 0.0
        num_d_mod = 0.0
        den_d_mod = 0.0
        den_e_mod = 0.0
        # We compute the iterations needed
        for j in range(0, len(bar_values)):
            num_r = num_r + ((bar_values[i, j] - np.mean(bar_values[i])) * (quadratic_function[i, j] -
                                                                            np.mean(quadratic_function[i])))
            den_r_poll = den_r_poll + (bar_values[i, j] - np.mean(bar_values[i])) ** 2
            den_r_quar = den_r_quar + (quadratic_function[i, j] - np.mean(quadratic_function[i])) ** 2
            num_d = num_d + (bar_values[i, j] - quadratic_function[i, j]) ** 2
            den_d = den_d + (np.abs(quadratic_function[i, j] - np.mean(bar_values[i])) +
                             np.abs(bar_values[i, j] - np.mean(bar_values[i]))) ** 2
            num_d_mod = num_d_mod + np.abs(bar_values[i, j] - quadratic_function[i, j])
            den_d_mod = den_d_mod + (np.abs(quadratic_function[i, j] - np.mean(bar_values[i])) +
                                     np.abs(bar_values[i, j] - np.mean(bar_values[i])))
            den_e_mod = den_e_mod + np.abs(bar_values[i, j] - np.mean(bar_values[i]))
        # We compute the efficiency coefficients of each month
        pearson_coefficient[i] = (num_r / (np.sqrt(den_r_poll) * np.sqrt(den_r_quar))) ** 2
        d_coefficient[i] = 1 - (num_d / den_d)
        e_coefficient[i] = 1 - (num_d / den_r_poll)
        d_mod_coefficient[i] = 1 - (num_d_mod / den_d_mod)
        e_mod_coefficient[i] = 1 - (num_d_mod / den_e_mod)

    return pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
