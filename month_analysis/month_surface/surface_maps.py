# encoding utf-8 #

import os
import matplotlib.pyplot as plt
import numpy as np
from constants import *


def maps_plotting(classified_lon, classified_lat, name, big_name, year, z):
    """"""

    # We get the username
    username = os.getlogin()

    # We start plotting the map
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    fig.patch.set_visible(False)
    ax.axis('off')
    fig.dpi = 300
    ax.scatter(classified_lon[0], classified_lat[0], marker='s', c=np.array([0, 0, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[1], classified_lat[1], marker='s', c=np.array([1, 0, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[2], classified_lat[2], marker='s', c=np.array([0, 1, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[3], classified_lat[3], marker='s', c=np.array([0, 0, 1]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[4], classified_lat[4], marker='s', c=np.array([1, 1, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[5], classified_lat[5], marker='s', c=np.array([1, 0, 1]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[6], classified_lat[6], marker='s', c=np.array([0, 1, 1]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[7], classified_lat[7], marker='s', c=np.array([1, 0.5, 0.5]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[8], classified_lat[8], marker='s', c=np.array([0.5, 1, 0.5]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[9], classified_lat[9], marker='s', c=np.array([0.5, 0.5, 1]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[10], classified_lat[10], marker='s', c=np.array([1, 0.5, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[11], classified_lat[11], marker='s', c=np.array([1, 0, 0.5]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[12], classified_lat[12], marker='s', c=np.array([0.5, 1, 0]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[13], classified_lat[13], marker='s', c=np.array([0, 1, 0.5]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[14], classified_lat[14], marker='s', c=np.array([0.5, 0, 1]), s=(72./fig.dpi)**2)
    ax.scatter(classified_lon[15], classified_lat[15], marker='s', c=np.array([0, 0.5, 1]), s=(72./fig.dpi)**2)
    plt.savefig(r'C:\Users\%s\Desktop\practicas_alvaro\images\surface_maps\%s_%s_%s_surface_map.tiff'
                % (username, name, year, str(z + 1)), dpi=300)
    plt.close()

    return


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
