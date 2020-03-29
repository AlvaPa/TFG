# encoding utf-8 #

import winsound
from month_analysis.month_efficiency import read_files_efficiency
from month_analysis.month_efficiency import efficiency_diagrams
from constants import *


def main_code():
    """"""

    # We initialize the variables containing the pollutant's names
    pollutants_names = [no2, ozone, pm_10, pm_2p5]
    pollutant_big_name = [NO2, OZONE, PM10, PM2P5]

    # We search for the root folder containing the files
    root = read_files_efficiency.path_finder()

    # We start the iterations to plot all the data
    for x in range(0, 4):
        # Pollutant which is going to be analyzed for the five years of data collected
        name = pollutants_names[x]
        big_name = pollutant_big_name[x]

        print('Plotting the efficiency coefficients of', name, '!\n')

        # We read the file
        r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
            read_files_efficiency.read(root, name)

        # We plot the boxes and whiskers plot
        efficiency_diagrams.boxplot(r_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient,
                                    name, big_name)

    # When the iterations have finished, the plotting is finished as well
    print('All data analyzed!')

    # We emit a beep to show that the code has finished
    winsound.Beep(2500, 500)

    return


if __name__ == '__main__':
    main_code()
