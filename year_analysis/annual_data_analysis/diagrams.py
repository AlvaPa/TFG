# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import numba
import os
from constants import *


def diagrams_representation(complete_pollution, name, years):
    """
    This is the main function to represent the boxplots, histograms and their smoothings. It also computes the
    efficiency coefficients to check if the histograms' smoothings are accurate.
    :param complete_pollution: Multiple array that holds of each pollutant per location [ug/m^3]
    :param name: Name of the pollutant we are analyzing
    :param years: Year we are analyzing
    :return: pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
    """

    # We get the username
    username = os.getlogin()

    "Boxplot"
    # We plot the boxplot
    boxplot(complete_pollution, name, years, username)

    "Histogram and parametric curve"
    # We compute the kernel density smoothing to plot it next to the histograms
    # We initialize some parameters
    h = np.array([0] * 5, dtype=float)
    quadratic_function = np.array([[0] * len(complete_pollution[0, ::]), [0] * len(complete_pollution[0, ::]),
                                   [0] * len(complete_pollution[0, ::]), [0] * len(complete_pollution[0, ::]),
                                   [0] * len(complete_pollution[0, ::])], dtype=float)
    # We compute the quadratic function
    quadratic_function = quadratic_kernel_plotting(complete_pollution, h, quadratic_function)

    # We plot the histogram and the parametric function
    bar_values, center_values = histogram(complete_pollution, name, years, quadratic_function, username)

    "Efficiency coefficients"
    # We initialize the coefficients to determine the efficiency of the parametric curves
    determination_coefficient = np.array([0] * 5, dtype=float)
    d_coefficient = np.array([0] * 5, dtype=float)
    e_coefficient = np.array([0] * 5, dtype=float)
    d_mod_coefficient = np.array([0] * 5, dtype=float)
    e_mod_coefficient = np.array([0] * 5, dtype=float)

    # We initialize the quadratic function used to compute the coefficients
    quadratic_efficiency_function = np.array([[0] * 130, [0] * 130, [0] * 130, [0] * 130, [0] * 130], dtype=float)

    # We compute the quadratic function's elements
    quadratic_efficiency_function = \
        quadratic_kernel_coefficients(complete_pollution, center_values, h, quadratic_efficiency_function)

    # We compute the efficiency coefficients
    determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
        efficiency_criteria(bar_values, quadratic_efficiency_function, determination_coefficient, d_coefficient,
                            e_coefficient, d_mod_coefficient, e_mod_coefficient)

    return determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient


def boxplot(complete_pollution, name, years, username):
    """
    This function depicts the boxplots of the pollution's data per year.
    :param complete_pollution: Multiple array that holds of each pollutant per location [ug/m^3]
    :param name: Name of the pollutant we are analyzing
    :param years: Year of the data we are analysing
    :param username: Username
    :return:
    """

    # Initialize dictionary to represent later the boxplot
    dictionary = {'2007': complete_pollution[0], '2008': complete_pollution[1], '2009': complete_pollution[2],
                  '2010': complete_pollution[3], '2011': complete_pollution[4]}

    # We start the parameters for the boxplot
    # We open the figure and axes
    fig = plt.figure(5, figsize=(18, 12))
    ax = fig.add_subplot(111)
    # Plotting style
    fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                  alpha=0.5)
    ax.set_axisbelow(True)
    # Labels
    ax.set_xlabel('Years', size=50)
    ax.set_ylabel(r'Concentration ($\frac{{\mu}g}{m^{3}}$)', size=50)
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.tick_params(axis='both', which='minor', labelsize=36)
    ax.set_xticklabels(years)
    # We establish the range of the plot
    if name == no2:
        ax.set_ylim(10, 80)
    elif name == ozone:
        ax.set_ylim(30, 80)
    elif name == pm_10:
        ax.set_ylim(15, 40)
    else:
        ax.set_ylim(5, 35)
    # We plot the box and whiskers
    ax.boxplot(dictionary.values())
    # We save the file
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\annual\annual_%s_boxplot.tiff'
                % (username, name), bbox_inches='tight', dpi=300)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\annual\annual_%s_boxplot.png'
                % (username, name), bbox_inches='tight', dpi=90)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\boxplots\annual\annual_%s_boxplot.jpg'
                % (username, name), bbox_inches='tight', quality=10)
    # We close the figure
    plt.close(5)

    return


def histogram(complete_pollution, name, years, quadratic_function, username):
    """
    This function represents the histogram and the parametric plot of the probabilities of the concentrations in the
    same diagram per month. It also computes the value where the probability of each bin is centered (in order to use it
    later to compute the efficiency coefficients).
    :param complete_pollution: Multiple array that holds of each pollutant per location [ug/m^3]
    :param name: Name of the pollutant we are analyzing
    :param years: Year we are analyzing
    :param quadratic_function: Histogram's smoothing
    :param username: Username
    :return: bar_values, center_values
    """

    # We initialize the variables
    # Number of bins
    n_bins = 130
    # Probability of each bin
    bar_values = np.array([[0] * n_bins, [0] * n_bins, [0] * n_bins, [0] * n_bins,
                           [0] * n_bins], dtype=float)
    # Pollution concentration at which the bin values are centered
    center_values = np.array([[0] * n_bins, [0] * n_bins, [0] * n_bins, [0] * n_bins, [0] * n_bins], dtype=float)

    for i in range(0, 5):
        # We compute the width of the bins
        pollution_range = np.max(complete_pollution[i, ::]) - np.min(complete_pollution[i, ::])
        width = float(pollution_range / (n_bins + 1))
        # We establish the year we are analyzing
        year = years[i]
        # We start plotting the histogram
        # We open the figure and axes
        fig = plt.figure(i, figsize=(9, 6))
        ax = fig.add_subplot(111)
        # Plotting style
        ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)
        ax.set_axisbelow(True)
        fig.tight_layout()
        # Labels
        ax.set_xlabel(r'Concentration ($\frac{{\mu}g}{m^{3}}$)', size=25)
        ax.set_ylabel('Probability density', size=25)
        ax.tick_params(axis='both', which='major', labelsize=18)
        ax.tick_params(axis='both', which='minor', labelsize=18)
        # We plot the histogram and the parametric curve
        output = ax.hist(complete_pollution[i, ::], bins=n_bins, density=True)  # Histogram
        ax.plot(complete_pollution[i, ::], quadratic_function[i, ::], '--', lw=1.5)     # Parametric curve
        ax.text(0.55, 0.95, r'Bandwidth = %f $\frac{{\mu}g}{m^{3}}$' % width,
                transform=ax.transAxes, size=13)
        # We save the file
        plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\histograms\annual\annual_%s_%s_histogram.tiff'
                    % (username, name, year), bbox_inches='tight', dpi=300)
        plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\histograms\annual\annual_%s_%s_histogram.png'
                    % (username, name, year), bbox_inches='tight', dpi=300)
        # We assign the bar probability values
        # We convert the output to arrays
        bar_probability = np.asarray(output[0])   # Probability of each bin
        bin_edges = np.asarray(output[1])   # Bin edges
        for j in range(0, n_bins):
            bar_values[i, j] = bar_probability[j]
            center_values[i, j] = round(bin_edges[j] + ((bin_edges[j + 1] - bin_edges[j]) / 2), 6)
        # We close the figure
        plt.close(i)

    return bar_values, center_values


@numba.jit(nopython=True)
def quadratic_kernel_plotting(complete_pollution, h, quadratic_function):
    """
    This function computes the histogram's smoothing that will be plotted along with the histogram. It computes the
    smoothing for every concentration available.
    :param complete_pollution:Multiple array that holds of each pollutant per location [ug/m^3]
    :param h: Bandwidth
    :param quadratic_function: Histogram's smoothing (using a quadratic kernel) used for plotting
    :return:quadratic_function
    """

    # We start computing the functions
    k_t = 0
    for i in range(0, 5):
        # Standard deviation
        s = np.std(complete_pollution[i, ::])
        # Number of elements
        n = len(complete_pollution[i, ::])
        # Bandwidth
        h[i] = 0.9 * s / (n ** 0.2)
        divisor = 1.0 / h[i]
        complete_pollution[i, ::] = np.sort(complete_pollution[i, ::])
        for j in range(0, n):
            for k in range(0, n):
                t = (complete_pollution[i, j] - complete_pollution[i, k]) * divisor
                if abs(t) < 1.0 and j != k:
                    k_t += 0.75 * (1 - t ** 2)
            constant = h[i] * n
            quadratic_function[i, j] = k_t / constant
            k_t = 0

    return quadratic_function


def quadratic_kernel_coefficients(complete_pollution, center_values, h, quadratic_efficiency_function):
    """
    This function computes the histogram's smoothing that will be used to compute the efficiency coefficients.
    It calculates the smoothing only for the values at which every bin is centered.
    :param complete_pollution: Multiple array that holds of each pollutant per location [ug/m^3]
    :param center_values: Values at which each bin is centered
    :param h: Bandwidth
    :param quadratic_efficiency_function: Histogram's smoothing used for computing efficiency coefficients
    :return: quadratic_efficiency_function
    """

    # We start computing the functions
    k_t = 0
    for i in range(0, 5):
        # Standard deviation
        s = np.std(complete_pollution[i, ::])
        # Number of elements
        n = len(complete_pollution[i, ::])
        # Bandwidth
        h[i] = 0.9 * s / (n ** 0.2)
        divisor = 1.0 / h[i]
        for j in range(0, len(center_values[i])):
            for k in range(0, n):
                t = (center_values[i, j] - complete_pollution[i, k]) * divisor
                if abs(t) < 1.0 and j != k:
                    k_t += 0.75 * (1 - t ** 2)
            constant = h[i] * n
            quadratic_efficiency_function[i, j] = k_t / constant
            k_t = 0     # We reset the kernel

    return quadratic_efficiency_function


def efficiency_criteria(bar_values, quadratic_efficiency_function, determination_coefficient, d_coefficient,
                        e_coefficient, d_mod_coefficient, e_mod_coefficient):
    """
    Function made to compute different efficiency coefficients to check if the histograms' smoothings are accurate. It
    computes the coefficient of determination r^2, index of agreement d, Nash-Sutcliffe efficiency E and the modified
    forms of d and E.
    :param bar_values: Probability of each bin
    :param quadratic_efficiency_function: Histogram's smoothing used for computing efficiency coefficients
    :param determination_coefficient: Coefficient of determination r^2
    :param d_coefficient: Index of agreement d
    :param e_coefficient: Nash-Sutcliffe efficiency E
    :param d_mod_coefficient: Modified form of d
    :param e_mod_coefficient: Modified form of E
    :return: pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
    """

    # We perform the calculations
    for i in range(0, 5):
        # We initialize some variables to perform to calculations
        num_r = 0.0
        den_r_poll = 0.0
        den_r_quar = 0.0
        num_d = 0.0
        den_d = 0.0
        num_d_mod = 0.0
        den_d_mod = 0.0
        den_e_mod = 0.0
        # We compute the iterations needed. All of this are sums.
        for j in range(0, len(bar_values)):
            num_r = num_r + ((bar_values[i, j] - np.mean(bar_values[i])) *
                             (quadratic_efficiency_function[i, j] - np.mean(quadratic_efficiency_function[i])))
            den_r_poll = den_r_poll + (bar_values[i, j] - np.mean(bar_values[i])) ** 2
            den_r_quar = (den_r_quar +
                          (quadratic_efficiency_function[i, j] - np.mean(quadratic_efficiency_function[i])) ** 2)
            num_d = num_d + (bar_values[i, j] - quadratic_efficiency_function[i, j]) ** 2
            den_d = den_d + (np.abs(quadratic_efficiency_function[i, j] - np.mean(bar_values[i])) +
                             np.abs(bar_values[i, j] - np.mean(bar_values[i]))) ** 2
            num_d_mod = num_d_mod + np.abs(bar_values[i, j] - quadratic_efficiency_function[i, j])
            den_d_mod = den_d_mod + (np.abs(quadratic_efficiency_function[i, j] - np.mean(bar_values[i])) +
                                     np.abs(bar_values[i, j] - np.mean(bar_values[i])))
            den_e_mod = den_e_mod + np.abs(bar_values[i, j] - np.mean(bar_values[i]))
        # We compute the efficiency coefficients of each month
        determination_coefficient[i] = round((num_r / (np.sqrt(den_r_poll) * np.sqrt(den_r_quar))) ** 2, 4)
        d_coefficient[i] = round(1 - (num_d / den_d), 4)
        e_coefficient[i] = round(1 - (num_d / den_r_poll), 4)
        d_mod_coefficient[i] = round(1 - (num_d_mod / den_d_mod), 4)
        e_mod_coefficient[i] = round(1 - (num_d_mod / den_e_mod), 4)

    return determination_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
