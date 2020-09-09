# encoding utf-8 #

import pandas as pd
import os
from constants import *


def output_and_closing(total_surface_percentage, name, years):
    """"""

    # We get the username
    username = os.getlogin()

    # We start the output of data
    if name == no2:
        no2_output(total_surface_percentage, name, years, username)
    elif name == ozone:
        ozone_output(total_surface_percentage, name, years, username)
    elif name == pm_10:
        pm10_output(total_surface_percentage, name, years, username)
    else:
        pm2p5_output(total_surface_percentage, name, years, username)

    return


def no2_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'years': years, '(0 - 40)': total_surface_percentage[0],
                       '(40 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def ozone_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 45)': total_surface_percentage[0],
                       '(45 - 60)': total_surface_percentage[1], '(60 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm10_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 20)': total_surface_percentage[0],
                       '(20 - 40)': total_surface_percentage[1], '(40 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm2p5_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 10)': total_surface_percentage[0],
                       '(10 - 25)': total_surface_percentage[1], '(25 and more)': total_surface_percentage[2]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return
