# encoding utf-8 #

import pandas as pd
import os
from constants import *


def output_and_closing(total_surface_percentage, name, year, months):
    """"""

    # We get the username
    username = os.getlogin()

    # We start the output of data
    if name == no2:
        no2_output(total_surface_percentage, name, year, months, username)
    elif name == ozone:
        ozone_output(total_surface_percentage, name, year, months, username)
    elif name == pm_10:
        pm10_output(total_surface_percentage, name, year, months, username)
    else:
        pm2p5_output(total_surface_percentage, name, year, months, username)

    return


def no2_output(total_surface_percentage, name, year, months, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'months': months, '(0 - 40)': total_surface_percentage[0],
                      '(40 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_%s_surface_percentage.txt'
              % (username, name, year), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def ozone_output(total_surface_percentage, name, year, months, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'months': months, '(0 - 100)': total_surface_percentage[0],
                       '(100 - 120)': total_surface_percentage[1], '(120 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_%s_surface_percentage.txt'
              % (username, name, year), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm10_output(total_surface_percentage, name, year, months, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'months': months, '(0 - 20)': total_surface_percentage[0],
                       '(20 - 40)': total_surface_percentage[1], '(40 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_%s_surface_percentage.txt'
              % (username, name, year), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm2p5_output(total_surface_percentage, name, year, months, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'months': months, '(0 - 10)': total_surface_percentage[0],
                       '(10 - 20)': total_surface_percentage[1], '(20 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_%s_surface_percentage.txt'
              % (username, name, year), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return
