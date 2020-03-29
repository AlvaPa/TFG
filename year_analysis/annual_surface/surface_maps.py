# encoding utf-8 #

import os
import matplotlib.pyplot as plt
import numpy as np
from constants import *


def maps_plotting(classified_lon, classified_lat, name, big_name, year):
    """"""

    # We get the username
    username = os.getlogin()

    # We start plotting the map
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.set_title('Concentration of %s in %s' % (big_name, year))
    fig.dpi = 300
    fig.tight_layout()

    # We plot all the points we've sorted
    ax.scatter(classified_lon[0], classified_lat[0], marker='s', c=np.array([0, 0, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[1], classified_lat[1], marker='s', c=np.array([1, 0, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[2], classified_lat[2], marker='s', c=np.array([0, 1, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[3], classified_lat[3], marker='s', c=np.array([0, 0, 1]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[4], classified_lat[4], marker='s', c=np.array([1, 1, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[5], classified_lat[5], marker='s', c=np.array([1, 0, 1]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[6], classified_lat[6], marker='s', c=np.array([0, 1, 1]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[7], classified_lat[7], marker='s', c=np.array([1, 0.5, 0.5]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[8], classified_lat[8], marker='s', c=np.array([0.5, 1, 0.5]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[9], classified_lat[9], marker='s', c=np.array([0.5, 0.5, 1]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[10], classified_lat[10], marker='s', c=np.array([1, 0.5, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[11], classified_lat[11], marker='s', c=np.array([1, 0, 0.5]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[12], classified_lat[12], marker='s', c=np.array([0.5, 1, 0]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[13], classified_lat[13], marker='s', c=np.array([0.3, 0.8, 0.6]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[14], classified_lat[14], marker='s', c=np.array([0.5, 0, 0.5]), s=(72. / fig.dpi) ** 2)
    ax.scatter(classified_lon[15], classified_lat[15], marker='s', c=np.array([0.3, 0.6, 0.8]), s=(72. / fig.dpi) ** 2)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\surface_maps\annual\%s_%s_surface_map.tiff'
                % (username, name, year), dpi=300)
    plt.close()

    return


def legend_maker(name, big_name):
    """"""

    # We get the username
    username = os.getlogin()

    # We start plotting the map
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    fig.patch.set_visible(False)
    ax.axis('off')
    fig.dpi = 300
    ax.set_ylim(-1, 5)
    ax.set_xlim(-1, 7)

    # We plot all the colors
    ax.scatter(0.5, 3.5, marker='s', c=np.array([0, 0, 0]), s=3000)
    ax.scatter(1.5, 3.5, marker='s', c=np.array([1, 0, 0]), s=3000)
    ax.scatter(2.5, 3.5, marker='s', c=np.array([0, 1, 0]), s=3000)
    ax.scatter(3.5, 3.5, marker='s', c=np.array([0, 0, 1]), s=3000)
    ax.scatter(0.5, 2.5, marker='s', c=np.array([1, 1, 0]), s=3000)
    ax.scatter(1.5, 2.5, marker='s', c=np.array([1, 0, 1]), s=3000)
    ax.scatter(2.5, 2.5, marker='s', c=np.array([0, 1, 1]), s=3000)
    ax.scatter(3.5, 2.5, marker='s', c=np.array([1, 0.5, 0.5]), s=3000)
    ax.scatter(0.5, 1.5, marker='s', c=np.array([0.5, 1, 0.5]), s=3000)
    ax.scatter(1.5, 1.5, marker='s', c=np.array([0.5, 0.5, 1]), s=3000)
    ax.scatter(2.5, 1.5, marker='s', c=np.array([1, 0.5, 0]), s=3000)
    ax.scatter(3.5, 1.5, marker='s', c=np.array([1, 0, 0.5]), s=3000)
    ax.scatter(0.5, 0.5, marker='s', c=np.array([0.5, 1, 0]), s=3000)
    ax.scatter(1.5, 0.5, marker='s', c=np.array([0.3, 0.8, 0.6]), s=3000)
    ax.scatter(2.5, 0.5, marker='s', c=np.array([0.5, 0, 0.5]), s=3000)
    ax.scatter(3.5, 0.5, marker='s', c=np.array([0.3, 0.6, 0.8]), s=3000)

    # We make groups for the legend
    group_1 = ax.scatter(10.5, 3.5, marker='s', c=np.array([0, 0, 0]), s=30)
    group_2 = ax.scatter(10.5, 3.5, marker='s', c=np.array([1, 0, 0]), s=30)
    group_3 = ax.scatter(20.5, 3.5, marker='s', c=np.array([0, 1, 0]), s=30)
    group_4 = ax.scatter(30.5, 3.5, marker='s', c=np.array([0, 0, 1]), s=30)
    group_5 = ax.scatter(10.5, 2.5, marker='s', c=np.array([1, 1, 0]), s=30)
    group_6 = ax.scatter(10.5, 2.5, marker='s', c=np.array([1, 0, 1]), s=30)
    group_7 = ax.scatter(20.5, 2.5, marker='s', c=np.array([0, 1, 1]), s=30)
    group_8 = ax.scatter(30.5, 2.5, marker='s', c=np.array([1, 0.5, 0.5]), s=30)
    group_9 = ax.scatter(10.5, 1.5, marker='s', c=np.array([0.5, 1, 0.5]), s=30)
    group_10 = ax.scatter(10.5, 1.5, marker='s', c=np.array([0.5, 0.5, 1]), s=30)
    group_11 = ax.scatter(20.5, 1.5, marker='s', c=np.array([1, 0.5, 0]), s=30)
    group_12 = ax.scatter(30.5, 1.5, marker='s', c=np.array([1, 0, 0.5]), s=30)
    group_13 = ax.scatter(10.5, 0.5, marker='s', c=np.array([0.5, 1, 0]), s=30)
    group_14 = ax.scatter(10.5, 0.5, marker='s', c=np.array([0.3, 0.8, 0.6]), s=30)
    group_15 = ax.scatter(20.5, 0.5, marker='s', c=np.array([0.5, 0, 0.5]), s=30)
    group_16 = ax.scatter(30.5, 0.5, marker='s', c=np.array([0.3, 0.6, 0.8]), s=30)

    # We select the ranges of the pollutant's concentrations for the legend
    if name == no2:
        groups = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9]
        labels = ['(0 - 5)', '(5 - 10)', '(10 - 15)', '(15 - 20)', '(20 - 25)', '(25 - 30)', '(30 - 35)', '(35 - 40)',
                  '(40 and on)']
    elif name == ozone:
        groups = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9, group_10, group_11,
                  group_12, group_13]
        labels = ['(0 - 10)', '(10 - 20)', '(20 - 30)', '(30 - 40)', '(40 - 50)', '(50 - 60)', '(60 - 70)', '(70 - 80)',
                  '(80 - 90)', '(90 - 100)', '(100 - 110)', '(110 - 120)', '(120 and on)']
    elif name == pm_10:
        groups = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9, group_10, group_11,
                  group_12, group_13, group_14, group_15, group_16]
        labels = ['(0 - 12)', '(12 - 14)', '(14 - 16)', '(16 - 18)', '(18 - 20)', '(20 - 22)', '(22 - 24)',
                  '(24 - 26)', '(26 - 28)', '(28 - 30)', '(30 - 32)', '(32 - 34)', '(34 - 36)', '(36 - 38)',
                  '(38 - 40)', '(40 and on)']
    else:
        groups = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9, group_10, group_11,
                  group_12, group_13, group_14, group_15, group_16]
        labels = ['(0 - 6)', '(6 - 7)', '(7 - 8)', '(8 - 9)', '(9 - 10)', '(10 - 11)', '(11 - 12)',
                  '(12 - 13)', '(13 - 14)', '(14 - 15)', '(15 - 16)', '(16 - 17)', '(17 - 18)', '(18 - 19)',
                  '(19 - 20)', '(20 and on)']

    # We make the legend
    legend = ax.legend(groups, labels, loc='upper right', title=r'Concentration of %s / $\frac{{\mu}g}{m^{3}}$'
                                                                % big_name)
    ax.add_artist(legend)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\surface_maps\legends\color_legend_%s.tiff'
                % (username, name), dpi=300)
    plt.close()

    return