# encoding utf-8 #

import numpy as np
import matplotlib.pyplot as plt
import numba
import os
from constants import *


def diagrams_representation(complete_pollution, name, big_name, years):
    """"""

    # We get the username
    username = os.getlogin()

    "Boxplot"
    # We plot the boxplot
    boxplot(complete_pollution, name, big_name, years, username)

    "Histogram and parametric curve"
    # We compute the kernel density smoothing to plot it next to the histograms
    # We initialize some parameters
    h = np.array([0] * 5, dtype=float)
    quadratic_function = np.array([[0] * len(complete_pollution[0, ::]), [0] * len(complete_pollution[0, ::]),
                                   [0] * len(complete_pollution[0, ::]), [0] * len(complete_pollution[0, ::]),
                                   [0] * len(complete_pollution[0, ::])], dtype=float)
    # We compute the quadratic function
    quadratic_function = quadratic_kernel(complete_pollution, h, quadratic_function)

    # We plot the histogram and the parametric function
    bar_values = histogram(complete_pollution, name, big_name, years, quadratic_function, username)

    "Efficiency coefficients"
    # We initialize the coefficients to determine the efficiency of the parametric curves
    pearson_coefficient = np.array([0] * 5, dtype=float)
    d_coefficient = np.array([0] * 5, dtype=float)
    e_coefficient = np.array([0] * 5, dtype=float)
    d_mod_coefficient = np.array([0] * 5, dtype=float)
    e_mod_coefficient = np.array([0] * 5, dtype=float)

    # We compute the efficiency coefficients
    pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
        efficiency_criteria(bar_values, quadratic_function, pearson_coefficient, d_coefficient, e_coefficient,
                            d_mod_coefficient, e_mod_coefficient)

    return pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient


def boxplot(complete_pollution, name, big_name, years, username):
    """"""

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
    # Title
    ax.set_title('Location boxplots of the annual concentrations of %s during the period 2007-2011' % big_name)
    # Labels
    ax.set_xlabel('Years')
    ax.set_ylabel(r'Concentration / $\frac{{\mu}g}{m^{3}}$')
    ax.set_xticklabels([years])
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


def histogram(complete_pollution, name, big_name, years, quadratic_function, username):
    """
    This function represents the histogram and the parametric plot of the probabilities of the concentrations in the
    same diagram per month
    :param complete_pollution:
    :param name:
    :param big_name:
    :param years:
    :param quadratic_function:
    :param username:
    :return: bar_values
    """
    # We initialize the array which will contain the probability of the bars of the histogram
    bar_values = np.array([[0] * len(complete_pollution[0, ::]), [0] * len(complete_pollution[1, ::]),
                           [0] * len(complete_pollution[2, ::]), [0] * len(complete_pollution[3, ::]),
                           [0] * len(complete_pollution[4, ::])], dtype=float)

    for i in range(0, 5):
        # We compute the width of the bins
        # Number of bins, according to the pollutant
        if name == no2:
            n_bins = 270
        elif name == pm_2p5:
            n_bins = 200
        else:
            n_bins = 130
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
        # Title
        ax.set_title('Location histogram and Epanechnikov density smoothing of the concentration of %s in %s'
                     % (big_name, year))
        # Labels
        ax.set_xlabel(r'Concentration / $\frac{{\mu}g}{m^{3}}$')
        ax.set_ylabel('Probability density')
        # We plot the histogram and the parametric curve
        output = ax.hist(complete_pollution[i, ::], bins=n_bins, density=True)  # Histogram
        ax.plot(complete_pollution[i, ::], quadratic_function[i, ::], '--', lw=1.5)     # Parametric curve
        ax.text(0.7, 0.95, r'Bin width = %f $\frac{{\mu}g}{m^{3}}$' % width, transform=ax.transAxes)
        # We save the file
        plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\histograms\annual\annual_%s_%s_histogram.tiff'
                    % (username, name, year), bbox_inches='tight', dpi=300)
        plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\histograms\annual\annual_%s_%s_histogram.png'
                    % (username, name, year), bbox_inches='tight', dpi=300)
        # We assign the bar probability values
        # We convert the output to array
        n = np.asarray(output[0])   # Probability of each bin
        interval_elements = int((len(complete_pollution[0]) / n_bins) + 1)    # Number of elements each interval has
        for j in range(0, len(n)):
            for k in range(0, interval_elements):
                m = j * interval_elements + k
                if m >= len(bar_values[0]):
                    break
                bar_values[i, m] = n[j]
        # We close the figure
        plt.close(i)

    return bar_values


@numba.jit(nopython=True)
def quadratic_kernel(complete_pollution, h, quadratic_function):
    """"""

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
                             (quadratic_function[i, j] - np.mean(quadratic_function[i])))
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
        pearson_coefficient[i] = round((num_r / (np.sqrt(den_r_poll) * np.sqrt(den_r_quar))) ** 2, 4)
        d_coefficient[i] = round(1 - (num_d / den_d), 4)
        e_coefficient[i] = round(1 - (num_d / den_r_poll), 4)
        d_mod_coefficient[i] = round(1 - (num_d_mod / den_d_mod), 4)
        e_mod_coefficient[i] = round(1 - (num_d_mod / den_e_mod), 4)

    return pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient
