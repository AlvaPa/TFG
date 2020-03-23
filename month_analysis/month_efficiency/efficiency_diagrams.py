# encoding utf-8 #

import os
import matplotlib.pyplot as plt
import numpy as np


def boxplot(r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient, name, big_name):
    """"""

    # We get the username
    username = os.getlogin()

    # We initialize a dictionary to hold all the coefficients
    dictionary = {'r_coefficient': r_coefficient, 'd_coefficient': d_coefficient, 'e_coefficient': e_coefficient,
                  'd_mod_coefficient': d_mod_coefficient, 'e_mod_coefficient': e_mod_coefficient}

    # We plot the box and whiskers plot for all the coefficients

    # Parameters
    labels = ['a', 'b', 'c', 'd', 'e']
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                  alpha=0.5)
    ax.set_axisbelow(True)
    ax.set_title('Efficiency coefficients for the %s' % big_name)
    ax.set_xlabel('Efficiency coefficients')
    ax.set_ylabel('Values')
    xtickNames = plt.setp(ax, xticklabels=labels)
    plt.setp(xtickNames)
    # We plot the box and whiskers
    ax.boxplot(dictionary.values())
    # We save the file
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\efficiency_boxplots\%s_efficiency_boxplot.tiff'
                % (username, name), dpi=300)
    # We close the figure
    plt.close()
