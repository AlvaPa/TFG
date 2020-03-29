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
    df = pd.DataFrame({'years': years, '(0 - 5)': total_surface_percentage[0],
                       '(5 - 10)': total_surface_percentage[1], '(10 - 15)': total_surface_percentage[2],
                       '(15 - 20)': total_surface_percentage[3], '(20 - 25)': total_surface_percentage[4],
                       '(25 - 30)': total_surface_percentage[5], '(30 - 35)': total_surface_percentage[6],
                       '(35 - 40)': total_surface_percentage[7], '(40 and more)': total_surface_percentage[8]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def ozone_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 10)': total_surface_percentage[0],
                       '(10 - 20)': total_surface_percentage[1], '(20 - 30)': total_surface_percentage[2],
                       '(30 - 40)': total_surface_percentage[3], '(40 - 50)': total_surface_percentage[4],
                       '(50 - 60)': total_surface_percentage[5], '(60 - 70)': total_surface_percentage[6],
                       '(70 - 80)': total_surface_percentage[7], '(80 - 90)': total_surface_percentage[8],
                       '(90 - 100)': total_surface_percentage[9], '(100 - 110)': total_surface_percentage[10],
                       '(110 - 120)': total_surface_percentage[11], '(120 and more)': total_surface_percentage[12]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm10_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 12)': total_surface_percentage[0],
                       '(12 - 14)': total_surface_percentage[1], '(14 - 16)': total_surface_percentage[2],
                       '(16 - 18)': total_surface_percentage[3], '(18 - 20)': total_surface_percentage[4],
                       '(20 - 22)': total_surface_percentage[5], '(22 - 24)': total_surface_percentage[6],
                       '(24 - 26)': total_surface_percentage[7], '(26 - 28)': total_surface_percentage[8],
                       '(28 - 30)': total_surface_percentage[9], '(30 - 32)': total_surface_percentage[10],
                       '(32 - 34)': total_surface_percentage[11], '(34 - 36)': total_surface_percentage[12],
                       '(36 - 38)': total_surface_percentage[13], '(38 - 40)': total_surface_percentage[14],
                       '(40 and more)': total_surface_percentage[15]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return


def pm2p5_output(total_surface_percentage, name, years, username):
    """"""

    # We generate the data frame to output
    df = pd.DataFrame({'year': years, '(0 - 6)': total_surface_percentage[0],
                       '(6- 7)': total_surface_percentage[1], '(7 - 8)': total_surface_percentage[2],
                       '(8 - 9)': total_surface_percentage[3], '(9 - 10)': total_surface_percentage[4],
                       '(10 - 11)': total_surface_percentage[5], '(11 - 12)': total_surface_percentage[6],
                       '(12 - 13)': total_surface_percentage[7], '(13 - 14)': total_surface_percentage[8],
                       '(14 - 15)': total_surface_percentage[9], '(15 - 16)': total_surface_percentage[10],
                       '(16 - 17)': total_surface_percentage[11], '(17 - 18)': total_surface_percentage[12],
                       '(18 - 19)': total_surface_percentage[13], '(19 - 20)': total_surface_percentage[14],
                       '(20 and more)': total_surface_percentage[15]})

    with open(r'C:\Users\%s\Desktop\practicas_alvaro\output_data\surface\%s_surface_percentage.txt'
              % (username, name), 'w+') as file:
        # We write the file
        df.to_csv(file, index=False, sep='\t')

    return
